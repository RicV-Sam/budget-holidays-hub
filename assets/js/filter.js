document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('guide-search');
    const filterButtons = document.querySelectorAll('.filter-btn');
    const guideCards = document.querySelectorAll('.guide-card');

    // Initialize Reading Progress Bar
    const siteNav = document.querySelector('.site-nav');
    if (siteNav) {
        // Initialize Scroll to Top Button
        const scrollTopBtn = document.createElement('button');
        scrollTopBtn.className = 'scroll-top';
        scrollTopBtn.setAttribute('aria-label', 'Scroll to top');
        scrollTopBtn.innerHTML = '<span aria-hidden="true">↑</span>';
        document.body.appendChild(scrollTopBtn);

        scrollTopBtn.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
            const skipLink = document.querySelector('.skip-link');
            if (skipLink) skipLink.focus();
        });

        const progressContainer = document.createElement('div');
        progressContainer.className = 'reading-progress-container';

        const progressBar = document.createElement('div');
        progressBar.className = 'reading-progress-bar';
        progressBar.setAttribute('role', 'progressbar');
        progressBar.setAttribute('aria-label', 'Reading progress');
        progressBar.setAttribute('aria-valuenow', '0');
        progressBar.setAttribute('aria-valuemin', '0');
        progressBar.setAttribute('aria-valuemax', '100');

        progressContainer.appendChild(progressBar);
        siteNav.appendChild(progressContainer);

        let ticking = false;
        window.addEventListener('scroll', () => {
            if (!ticking) {
                window.requestAnimationFrame(() => {
                    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
                    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
                    const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
                    progressBar.style.width = scrolled + '%';
                    progressBar.setAttribute('aria-valuenow', Math.round(scrolled).toString());
                    scrollTopBtn.classList.toggle('visible', winScroll > 400);
                    ticking = false;
                });
                ticking = true;
            }
        });
    }

    // Initialize Clear Search Button
    if (searchInput) {
        const searchWrapper = searchInput.parentElement;
        if (searchWrapper && searchWrapper.classList.contains('search-wrapper')) {
            const clearBtn = document.createElement('button');
            clearBtn.className = 'search-clear-btn';
            clearBtn.setAttribute('aria-label', 'Clear search');
            clearBtn.type = 'button';
            clearBtn.innerHTML = '×';
            clearBtn.style.display = 'none'; // Initial state

            clearBtn.addEventListener('click', () => {
                searchInput.value = '';
                clearBtn.style.display = 'none';
                searchInput.focus();
                filterGuides();
            });

            searchWrapper.appendChild(clearBtn);

            searchInput.addEventListener('input', () => {
                clearBtn.style.display = searchInput.value ? 'block' : 'none';
            });

            // Initialize ARIA live announcer for search results
            const announcer = document.createElement('div');
            announcer.id = 'search-results-announcer';
            announcer.className = 'visually-hidden';
            announcer.setAttribute('aria-live', 'polite');
            searchWrapper.appendChild(announcer);
        }
    }

    function filterGuides() {
        const searchTerm = searchInput.value.toLowerCase();
        const section = searchInput.closest('section');
        if (!section) return;

        // Get all active filters within the current section (intersection)
        const activeFilters = Array.from(section.querySelectorAll('.filter-btn.active'))
            .map(btn => btn.dataset.filter);

        let visibleCount = 0;
        const grid = section.querySelector('.guides-grid');
        if (!grid) return;

        const cards = grid.querySelectorAll('.guide-card');

        cards.forEach(card => {
            const title = card.querySelector('h3').textContent.toLowerCase();
            const description = card.querySelector('p').textContent.toLowerCase();
            const category = card.dataset.category;
            const filterTags = card.dataset.filterTags ? card.dataset.filterTags.split(' ') : [];

            const matchesSearch = title.includes(searchTerm) || description.includes(searchTerm);

            const matchesFilters = activeFilters.every(filter => {
                if (filter === 'all') return true;
                return category === filter || filterTags.includes(filter);
            });

            if (matchesSearch && matchesFilters) {
                card.style.display = 'flex';
                card.classList.remove('hidden');
                visibleCount++;
            } else {
                card.style.display = 'none';
                card.classList.add('hidden');
            }
        });

        updateNoResultsMessage(grid, visibleCount);

        // Update visible results status
        const resultsStatus = section.querySelector('.results-status');
        if (resultsStatus) {
            const hasActiveFilter = activeFilters.some(f => f !== 'all');
            if ((searchTerm || hasActiveFilter) && visibleCount > 0) {
                resultsStatus.textContent = `Showing ${visibleCount} guide${visibleCount === 1 ? '' : 's'}`;
                resultsStatus.classList.add('visible');
            } else {
                resultsStatus.textContent = '';
                resultsStatus.classList.remove('visible');
            }
        }

        // Update ARIA live announcer with results count
        const announcer = document.getElementById('search-results-announcer');
        if (announcer) {
            announcer.textContent = visibleCount === 0
                ? 'No guides found matching your criteria.'
                : `${visibleCount} guide${visibleCount === 1 ? '' : 's'} found.`;
        }
    }

    function updateNoResultsMessage(container, count) {
        let messageElement = container.querySelector('.no-results');

        if (count === 0) {
            if (!messageElement) {
                messageElement = document.createElement('div');
                messageElement.className = 'no-results';
                messageElement.setAttribute('role', 'alert');
                messageElement.innerHTML = `
                    <span class="no-results-icon" aria-hidden="true">🔍</span>
                    <p>No guides found matching your criteria.</p>
                    <span class="no-results-tip">Try adjusting your search or filters.</span>
                    <button class="clear-filters-btn" aria-label="Clear all search and region filters">Clear all filters</button>
                `;

                const clearBtn = messageElement.querySelector('.clear-filters-btn');
                clearBtn.addEventListener('click', () => {
                    if (searchInput) {
                        searchInput.value = '';
                        const wrapper = searchInput.closest('.search-wrapper');
                        const searchClearBtn = wrapper ? wrapper.querySelector('.search-clear-btn') : null;
                        if (searchClearBtn) searchClearBtn.style.display = 'none';
                        searchInput.focus();
                    }

                    document.querySelectorAll('.filter-btn').forEach(btn => {
                        const isAll = btn.dataset.filter === 'all';
                        btn.classList.toggle('active', isAll);
                        btn.setAttribute('aria-selected', isAll ? 'true' : 'false');
                    });

                    filterGuides();
                });

                container.appendChild(messageElement);
            }
        } else if (messageElement) {
            messageElement.remove();
        messageElement = null;
        }
    }

    if (searchInput) {
        searchInput.addEventListener('input', filterGuides);

        // Support Escape key to clear search or blur if empty
        searchInput.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                if (searchInput.value === '') {
                    searchInput.blur();
                } else {
                    searchInput.value = '';
                    const wrapper = searchInput.closest('.search-wrapper');
                    const clearBtn = wrapper ? wrapper.querySelector('.search-clear-btn') : null;
                    if (clearBtn) clearBtn.style.display = 'none';
                    filterGuides();
                }
            }
        });
    }

    // Support keyboard shortcut (/) to focus search
    document.addEventListener('keydown', (e) => {
        if (e.key === '/' && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
            if (searchInput) {
                e.preventDefault();
                searchInput.scrollIntoView({ behavior: 'smooth', block: 'center' });
                searchInput.focus();
            }
        }
    });

    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Scope activation to the same tablist to support independent filter categories
            const tabList = button.closest('[role="tablist"]');
            const relatedButtons = tabList ? tabList.querySelectorAll('.filter-btn') : [button];

            relatedButtons.forEach(btn => {
                btn.classList.remove('active');
                btn.setAttribute('aria-selected', 'false');
            });

            button.classList.add('active');
            button.setAttribute('aria-selected', 'true');

            filterGuides();
        });
    });

    // Support keyboard navigation (Arrow Keys) for tablists
    document.querySelectorAll('[role="tablist"]').forEach(tabList => {
        tabList.addEventListener('keydown', (e) => {
            const buttons = Array.from(tabList.querySelectorAll('.filter-btn'));
            const currentIndex = buttons.indexOf(document.activeElement);
            if (currentIndex === -1) return;

            let nextIndex;
            if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
                nextIndex = (currentIndex + 1) % buttons.length;
            } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
                nextIndex = (currentIndex - 1 + buttons.length) % buttons.length;
            } else if (e.key === 'Home') {
                nextIndex = 0;
            } else if (e.key === 'End') {
                nextIndex = buttons.length - 1;
            } else {
                return;
            }

            e.preventDefault();
            buttons[nextIndex].focus();
        });
    });

    initShareButton();
});

function initShareButton() {
    const metaContainer = document.querySelector('.article-layout .meta, .article-layout .last-updated');
    if (!metaContainer) return;

    const shareBtn = document.createElement('button');
    shareBtn.className = 'filter-btn share-btn';
    shareBtn.style.marginLeft = '12px';
    shareBtn.style.padding = '6px 14px';
    shareBtn.style.fontSize = '0.85rem';
    shareBtn.innerHTML = '<span aria-hidden="true" style="margin-right: 6px;">🔗</span> Share Guide';

    shareBtn.addEventListener('click', async () => {
        const shareData = {
            title: document.title,
            url: window.location.href
        };

        try {
            if (navigator.share) {
                await navigator.share(shareData);
            } else {
                await navigator.clipboard.writeText(window.location.href);
                const originalText = shareBtn.innerHTML;
                shareBtn.innerHTML = '<span aria-hidden="true" style="margin-right: 6px;">✅</span> Copied!';
                shareBtn.classList.add('active');
                setTimeout(() => {
                    shareBtn.innerHTML = originalText;
                    shareBtn.classList.remove('active');
                }, 2000);
            }
        } catch (err) {
            console.log('Share failed:', err);
        }
    });

    metaContainer.appendChild(shareBtn);
}

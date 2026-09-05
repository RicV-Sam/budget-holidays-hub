(function () {
    function parsePayload(raw) {
        if (!raw) return {};
        try {
            return JSON.parse(raw);
        } catch (error) {
            return {};
        }
    }

    function trackTasteWorldEvent(eventName, payload) {
        if (!eventName || typeof window.gtag !== "function") return;
        window.gtag("event", eventName, payload || {});
    }

    document.addEventListener("DOMContentLoaded", function () {
        var viewEvent = document.body.getAttribute("data-taste-world-view");
        var viewPayload = parsePayload(document.body.getAttribute("data-taste-world-payload"));
        trackTasteWorldEvent(viewEvent, viewPayload);

        document.querySelectorAll("[data-track-event]").forEach(function (link) {
            link.addEventListener("click", function () {
                var eventName = link.getAttribute("data-track-event");
                var payload = parsePayload(link.getAttribute("data-track-payload"));
                trackTasteWorldEvent(eventName, payload);
            });
        });
    });
})();

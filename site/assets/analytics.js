// Google Analytics 4 for the AI Construct Lexis.
//
// The measurement ID is public by design: it is readable in the page source of
// any site that uses Google Analytics. It only lets a holder send hits to the
// property, never read its reports.
//
// Local development is excluded, so pages opened from a localhost server or
// straight off disk send nothing to the live property. Append ?ga_debug=1 to
// any URL to watch the events in the console without contacting Google.
(function () {
    'use strict';

    var ID = 'G-E7Q0LEXX5B';

    var host = location.hostname;
    var isLocal = !host ||
        host === 'localhost' || host === '127.0.0.1' || host === '::1' ||
        /\.(localhost|test|local)$/.test(host) ||
        location.protocol === 'file:';
    var DEBUG = /(?:^|[?&])ga_debug=1(?:&|$)/.test(location.search);

    if (isLocal && !DEBUG) return;

    window.dataLayer = window.dataLayer || [];
    // Exposed as window.gtag so later pages or handlers can send their own events.
    var gtag = window.gtag = function () {
        window.dataLayer.push(arguments);
        if (DEBUG) { try { console.log('[ga]', Array.prototype.slice.call(arguments)); } catch (e) { } }
    };
    gtag('js', new Date());
    gtag('config', ID);

    // The real tag is never loaded from a local page, even in debug mode.
    if (!isLocal) {
        var s = document.createElement('script');
        s.async = true;
        s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(ID);
        document.head.appendChild(s);
    }

    // --------------------------------------------------------------- events
    //
    // GA4 records page_view by itself on every real page load, which already
    // covers the eight pages. What follows covers the navigation that happens
    // inside a page with no load, and would otherwise be invisible.
    //
    // Selections are reported as counts and types, never as the construct or
    // instrument names a visitor chose.

    var PAGE = location.pathname.split('/').pop() || 'index.html';

    var TOOL = {
        'tools.html': 'index',
        'tools_confirmatory.html': 'confirmatory',
        'tools_overlap.html': 'overlap',
        'tools_instrument.html': 'instrument',
        'tools_claim.html': 'claim'
    };

    // Set once the visitor has actually done something. The tools pages mirror
    // their default state into the URL during first render; that is already
    // implied by page_view, so it is not reported as a query.
    var interacted = false;

    function attach() {
        ['pointerdown', 'keydown', 'change'].forEach(function (t) {
            document.addEventListener(t, function () { interacted = true; }, true);
        });

        // view_network.html: the Home / Constructs / Behavioral Indicators /
        // Measurement Instruments tabs swap the list in place.
        document.addEventListener('click', function (ev) {
            var el = ev.target;
            if (!el || typeof el.closest !== 'function') return;
            var btn = el.closest('.filter-btn[data-type]');
            if (btn) gtag('event', 'view_switch', { view: btn.getAttribute('data-type') || 'unknown' });
        }, true);

        // view_network.html: opening an entity page. selectNode is the single
        // function every path funnels through: result clicks call it directly,
        // and selectNodeByName (relationship rows, ?node= deep links) resolves
        // to a key and calls it too. Its argument is "<type>_<name>", where the
        // name itself may contain underscores, so only the first one splits.
        if (typeof window.selectNode === 'function') {
            var origSelect = window.selectNode;
            window.selectNode = function (nodeKey) {
                try {
                    var k = String(nodeKey == null ? '' : nodeKey);
                    var cut = k.indexOf('_');
                    gtag('event', 'entity_view', {
                        entity_type: cut > 0 ? k.slice(0, cut) : 'unknown',
                        entity_name: (cut > 0 ? k.slice(cut + 1) : k).slice(0, 100)
                    });
                } catch (e) { /* tracking must never break navigation */ }
                return origSelect.apply(this, arguments);
            };
        }

        // The tools and graph pages mirror every control change into the URL
        // with replaceState. Debounced, so ticking five boxes reports one
        // settled query rather than five partial ones.
        var timer = null;
        function schedule() {
            clearTimeout(timer);
            timer = setTimeout(report, 1500);
        }

        function pipeCount(v) { return v ? v.split('|').filter(Boolean).length : 0; }
        function num(v, dflt) { var n = parseInt(v, 10); return isNaN(n) ? dflt : n; }

        // Both pages leave a parameter out of the URL when it is at its
        // default, so an absent parameter reports the default value rather
        // than nothing.
        function report() {
            if (!interacted) return;
            var p = new URLSearchParams(location.search);
            if (Object.prototype.hasOwnProperty.call(TOOL, PAGE)) {
                var q = {
                    tool: TOOL[PAGE],
                    n_constructs: pipeCount(p.get('c')),
                    n_instruments: pipeCount(p.get('m')),
                    min_papers: num(p.get('min'), 2),
                    cross_type: p.get('x') === '1' ? 1 : 0,
                    methods_included: p.get('meth') === '0' ? 0 : 1,
                    venues_filtered: p.has('v') ? 1 : 0,
                    n_excluded: pipeCount(p.get('ex')),
                    n_included: pipeCount(p.get('in'))
                };
                if (p.get('tab')) q.tab = p.get('tab');
                if (p.get('k')) q.top_k = num(p.get('k'), 5);
                gtag('event', 'tool_query', q);
            } else if (PAGE === 'network_graph.html') {
                gtag('event', 'graph_query', {
                    n_selected: (p.get('sel') || '').split(',').filter(Boolean).length,
                    induced: p.get('view') === 'induced' ? 1 : 0,
                    edge_open: p.get('edge') ? 1 : 0,
                    focused: p.get('focus') === '1' ? 1 : 0,
                    unlinked: p.get('unlinked') === '1' ? 1 : 0,
                    min_papers: num(p.get('min_papers'), 2),
                    show_level: p.get('show') || '50',
                    types_filtered: p.has('types') ? 1 : 0,
                    entities_filtered: p.has('entities') ? 1 : 0
                });
            }
        }

        ['replaceState', 'pushState'].forEach(function (m) {
            var native = history[m];
            if (typeof native !== 'function') return;
            history[m] = function () {
                var r = native.apply(history, arguments);
                try { schedule(); } catch (e) { }
                return r;
            };
        });
    }

    // Page scripts load at the end of <body>, so wait for them to define their
    // functions before wrapping anything.
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', attach);
    } else {
        attach();
    }
})();

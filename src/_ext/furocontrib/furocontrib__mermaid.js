// Configuration Constants
const MERMAID_CONTAINER_SELECTOR = 'div.mermaid';
const DARK_MODE_DIV_SELECTOR = '.mermaid._only-dark';
const LIGHT_MODE_DIV_SELECTOR = '.mermaid._only-light';
const MERMAID_CONFIG = {
    startOnLoad: true,
    flowchart: {
        htmlLabels: true,
        securityLevel: 'loose'
    }
};

/**
 * Initializes and renders a Mermaid diagram inside a given HTML element.
 *
 * @param {HTMLElement} mermaidDiv - The container div for the Mermaid diagram.
 * @param {object} config - Configuration object for the Mermaid diagram.
 */
function loadAndRenderMermaid(mermaidDiv, config) {
    // mermaidDiv.innerHTML = mermaidDiv.textContent;
    // console.log(mermaidDiv.textContent)
    mermaidDiv.classList.add('mermaid');
    merged_config = Object.assign({}, MERMAID_CONFIG, config);
    mermaid.initialize(merged_config, mermaidDiv);
    // mermaid.init(undefined, mermaidDiv);
}

/**
 * Handles the initial loading of Mermaid diagrams on page load.
 */
function initializeMermaidDiagrams() {
    const mermaidDivs = document.querySelectorAll(MERMAID_CONTAINER_SELECTOR);
    mermaidDivs.forEach(div => {
        loadAndRenderMermaid(div, JSON.parse(div.getAttribute('data-mermaid-config') || '{}'));
    });
}

/**
 * Updates the visibility of Mermaid diagrams based on the current theme.
 */
function updateThemeVisibility() {
    const theme = document.body.getAttribute('data-theme');
    const isDarkMode = theme === 'dark' || (theme === 'auto' && window.matchMedia('(prefers-color-scheme: dark)').matches);
    const isLightMode = theme === 'light' || (theme === 'auto' && window.matchMedia('(prefers-color-scheme: light)').matches);

    const darkDivs = document.querySelectorAll(DARK_MODE_DIV_SELECTOR);
    const lightDivs = document.querySelectorAll(LIGHT_MODE_DIV_SELECTOR);

    const updateVisibility = (divs, isVisible) => {
        divs.forEach(div => {
            div.style.visibility = isVisible ? 'visible' : 'hidden';
        });
    };

    updateVisibility(darkDivs, isDarkMode);
    updateVisibility(lightDivs, isLightMode);
}

// Event listener for DOMContentLoaded to initialize Mermaid diagrams
document.addEventListener("DOMContentLoaded", function () {
    initializeMermaidDiagrams();

    // MutationObserver for dynamic theme changes
    const observer = new MutationObserver(mutations => {
        mutations.forEach(mutation => {
            if (mutation.type === "attributes" && mutation.attributeName === "data-theme") {
                updateThemeVisibility();
            }
        });
    });

    observer.observe(document.body, {attributes: true});
    updateThemeVisibility();
});

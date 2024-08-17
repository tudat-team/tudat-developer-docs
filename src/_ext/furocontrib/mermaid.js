/**
 * Fetches, loads, and renders a Mermaid diagram based on configuration.
 * @param {HTMLElement} mermaidDiv - The container div for the Mermaid diagram.
 */
function loadAndRenderMermaid(mermaidDiv) {
    const mermaidFilePath = mermaidDiv.getAttribute('data-mermaid-file');
    const config = JSON.parse(mermaidDiv.getAttribute('data-mermaid-config') || '{}');

    console.log('Loading Mermaid diagram:', mermaidFilePath);
    console.log('Mermaid configuration:', config);

    fetch(mermaidFilePath)
        .then(response => response.text())
        .then(graphDefinition => {
            mermaidDiv.innerHTML = graphDefinition;
            mermaidDiv.classList.add('mermaid');
            mermaid.initialize(config, mermaidDiv);
            mermaid.init(undefined, mermaidDiv);
        })
        .catch(error => {
            console.error('Error loading Mermaid diagram:', error);
            mermaidDiv.textContent = 'Error loading diagram.';
        });
}


/**
 * Initialize table resizing and Mermaid diagram rendering after DOM content is loaded.
 */
document.addEventListener("DOMContentLoaded", function () {
    resizeTables();
    const mermaidDivs = document.querySelectorAll('div[data-mermaid-file]');
    mermaidDivs.forEach(div => loadAndRenderMermaid(div));
});
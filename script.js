// Global variables
let codeExamplesData = null;

// Slider value mappings (discrete values)
const dataDependencyValues = {
    0: 'None',
    1: 'Sequential',
    2: 'Non-sequential',
    3: 'Shared'
};

const codePatternValues = {
    0: 'None',
    1: 'Concatenation',
    2: 'Inclusion',
    3: 'Interleaved'
};

const repetitionValues = {
    0: 'None',
    1: 'Identical',
    2: 'Variable Included',
    3: 'Variable Scaled'
};

const colorClasses = {
    0: "highlight-blue",
    1: "highlight-orange",
    2: "highlight-green"
};

// Initialize the page
document.addEventListener('DOMContentLoaded', function() {
    loadCodeExamples();
    initializeSliders();
    initializeTabs();
    initializeShowExamplesButton();
    initializeTooltips();
});

// Load code examples from JSON file
async function loadCodeExamples() {
    try {
        const response = await fetch('code-examples.json');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        codeExamplesData = await response.json();
        loadCurrentExample('rose');
    } catch (error) {
        console.error('Error loading code examples:', error);
        // display error 
    }
}

// Load a specific example
function loadCurrentExample(exampleKey) {
    if (!codeExamplesData || !codeExamplesData.examples[exampleKey]) {
        return;
    }
    
    const example = codeExamplesData.examples[exampleKey];
    
    // Update code blocks
    // document.getElementById('unrefactored-title').textContent = example.unrefactored.title;
    // document.getElementById('refactored-title').textContent = example.refactored.title;
    
    // Apply highlights to refactored code
    let refactoredCode = example.refactored;
    example.highlights.forEach((highlight,index) => {
        const highlightedCode = `<span class="${getValue(colorClasses,index%3)}">${highlight}</span>`;
        refactoredCode = refactoredCode.replace(highlight, highlightedCode);
    });

    // Update description
    document.getElementById('example-prompt').textContent = example.prompt;
    document.getElementById('example-explanation').textContent = example.explanation;
    document.getElementById('example').textContent = example.title;
    
    document.getElementById('unrefactored-code').textContent = example.unrefactored;
    document.getElementById('refactored-code').innerHTML = refactoredCode;


}

function initializeSliders() {
    // Sliders now only show tick labels, no dynamic value updates needed
    // The discrete values are handled by the HTML step attribute
}


function initializeTabs() {
    const tabButtons = document.querySelectorAll('.tab-button');
    const tabContents = document.querySelectorAll('.tab-content');
    
    tabButtons.forEach(button => {
        button.addEventListener('click', function() {
            const targetTab = this.getAttribute('data-tab');
            
            // Remove active class from all buttons and contents
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));
            
            // Add active class to clicked button and corresponding content
            this.classList.add('active');
            document.getElementById(targetTab).classList.add('active');
        });
    });
}

function initializeShowExamplesButton() {
    const showExamplesBtn = document.querySelector('.show-examples-btn');

    showExamplesBtn.addEventListener('click', function() {
        // Add loading state
        this.classList.add('loading');
        this.disabled = true;

        // Get current slider values
        const dataDependency = document.getElementById('data-dependency').value;
        const codePattern = document.getElementById('code-pattern').value;
        const repetition = document.getElementById('repetition').value;

        // Ensure examples are loaded
        if (!codeExamplesData) {
            console.error('Code examples not loaded yet');
            this.classList.remove('loading');
            this.disabled = false;
            return;
        }

        // Get the human-readable values
        const dataDepValue = getValue(dataDependencyValues, parseInt(dataDependency));
        const codePatternValue = getValue(codePatternValues, parseInt(codePattern));
        const repetitionValue = getValue(repetitionValues, parseInt(repetition));

        // Simulate slight delay for better UX (shows loading state)
        setTimeout(() => {
            // Find all matching examples
            const matchingExamples = findMatchingExamples(dataDepValue, codePatternValue, repetitionValue);

            // Display results
            if (matchingExamples.length > 0) {
                displayMatchingExamples(matchingExamples);
            } else {
                displayNoMatches(dataDepValue, codePatternValue, repetitionValue);
            }

            // Remove loading state
            this.classList.remove('loading');
            this.disabled = false;

            // Add visual feedback
            const originalBg = this.style.background;
            this.style.background = '#1e8449';
            setTimeout(() => {
                this.style.background = originalBg;
            }, 200);
        }, 300);
    });
}

// Find examples that match the selected pattern criteria
function findMatchingExamples(dataDep, codePattern, repetition) {
    const matches = [];

    if (!codeExamplesData || !codeExamplesData.examples) {
        return matches;
    }

    for (const [key, example] of Object.entries(codeExamplesData.examples)) {
        const metadata = example.metadata;

        if (!metadata) continue;

        // Check if this example matches all three criteria
        const dataDependencyMatch = metadata.dataDependency === dataDep;
        const codePatternMatch = metadata.codePattern === codePattern;
        const repetitionMatch = metadata.repetition === repetition;

        if (dataDependencyMatch && codePatternMatch && repetitionMatch) {
            matches.push({ key, example });
        }
    }

    return matches;
}

// Display multiple matching examples by creating tabs
function displayMatchingExamples(matches) {
    const examplesSection = document.querySelector('.examples-section');

    // Clear existing tabs and content
    const tabsContainer = document.querySelector('.tabs');
    tabsContainer.innerHTML = '';

    // Remove old tab content divs
    const oldTabContents = document.querySelectorAll('.tab-content');
    oldTabContents.forEach(content => content.remove());

    // Create tabs and content for each match
    matches.forEach((match, index) => {
        const {key, example} = match;
        const isActive = index === 0;

        // Create tab button
        const tabButton = document.createElement('button');
        tabButton.className = `tab-button ${isActive ? 'active' : ''}`;
        tabButton.setAttribute('data-tab', key);
        tabButton.textContent = example.title;
        tabsContainer.appendChild(tabButton);

        // Create tab content
        const tabContent = document.createElement('div');
        tabContent.className = `tab-content ${isActive ? 'active' : ''}`;
        tabContent.id = key;
        tabContent.innerHTML = `
            <div class="code-comparison">
                <div class="code-block">
                    <h4>Raw</h4>
                    <div class="code-container">
                        <pre><code>${escapeHtml(example.unrefactored)}</code></pre>
                    </div>
                </div>

                <div class="code-block">
                    <h4>Decomposed</h4>
                    <div class="code-container">
                        <pre><code>${applyHighlights(example.refactored, example.highlights)}</code></pre>
                    </div>
                </div>
            </div>
        `;
        examplesSection.appendChild(tabContent);
    });

    // Re-initialize tab click handlers
    initializeTabs();

    // Display the first example's description
    const firstExample = matches[0].example;
    document.getElementById('example-prompt').textContent = firstExample.prompt;
    document.getElementById('example-patterns').textContent = firstExample.patterns;
    document.getElementById('example-explanation').textContent = firstExample.explanation;
}

// Display message when no examples match the criteria
function displayNoMatches(dataDep, codePattern, repetition) {
    // Clear existing tabs
    const tabsContainer = document.querySelector('.tabs');
    tabsContainer.innerHTML = '<div style="padding: 15px; text-align: center; color: #e74c3c; font-weight: 600;">No matching examples found</div>';

    // Remove old tab content
    const oldTabContents = document.querySelectorAll('.tab-content');
    oldTabContents.forEach(content => content.remove());



    // Create a message div
    const messageContent = document.createElement('div');
    messageContent.className = 'tab-content active';
    messageContent.innerHTML = `
        <div style="padding: 40px; text-align: center;">
            <h3 style="color: #e74c3c; margin-bottom: 20px;">Oups ... </h3>
            <p style="color: #7f8c8d; margin-bottom: 10px;">No code examples match the following criteria:</p>
            <ul style="list-style: none; padding: 0; color: #34495e;">
                <li><strong>Data Dependency:</strong> ${dataDep}</li>
                <li><strong>Code Pattern:</strong> ${codePattern}</li>
                <li><strong>Repetition:</strong> ${repetition}</li>
            </ul>
            <p style="color: #7f8c8d; margin-top: 20px;">Contact us for more information or to add code examples. Thank you!</p>
        </div>
    `;

    const examplesSection = document.querySelector('.examples-section');
    examplesSection.removeChild(document.querySelector('.description-section'));
    examplesSection.appendChild(messageContent);
}

// Helper function to escape HTML
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Helper function to apply highlights to code
function applyHighlights(code, highlights) {
    let highlightedCode = escapeHtml(code);

    if (!highlights || highlights.length === 0) {
        return highlightedCode;
    }


    highlights.forEach((highlight,index) => {
        const escapedPattern = escapeHtml(highlight);
        const highlightedPattern = `<span class="${getValue(colorClasses,index%3)}">${escapedPattern}</span>`;
        highlightedCode = highlightedCode.replace(new RegExp(escapedPattern.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g'), highlightedPattern);
    });

    return highlightedCode;
}

function getValue(valueMap, targetValue) {
    return valueMap[targetValue];
}

// Initialize tooltip functionality
function initializeTooltips() {
    const infoIcons = document.querySelectorAll('.info-icon');

    infoIcons.forEach(icon => {
        icon.addEventListener('click', function(e) {
            e.stopPropagation();
            const tooltipId = 'tooltip-' + this.getAttribute('data-tooltip');
            const tooltip = document.getElementById(tooltipId);

            // Close all other tooltips
            document.querySelectorAll('.tooltip').forEach(t => {
                if (t.id !== tooltipId) {
                    t.classList.remove('active');
                }
            });

            // Toggle current tooltip
            tooltip.classList.toggle('active');
        });
    });

    // Close tooltips when clicking outside
    document.addEventListener('click', function(e) {
        if (!e.target.classList.contains('info-icon')) {
            document.querySelectorAll('.tooltip').forEach(tooltip => {
                tooltip.classList.remove('active');
            });
        }
    });
}

// Add smooth scrolling for better UX
document.addEventListener('DOMContentLoaded', function() {
    // Add smooth transitions to all interactive elements
    const interactiveElements = document.querySelectorAll('.tab-button, .show-examples-btn, .slider');
    
    interactiveElements.forEach(element => {
        element.style.transition = 'all 0.3s ease';
    });
});

// Add keyboard navigation support
document.addEventListener('keydown', function(e) {
    if (e.key === 'Tab') {
        // Add focus indicators for accessibility
        document.addEventListener('keyup', function(e) {
            if (e.key === 'Tab') {
                document.body.classList.add('keyboard-navigation');
            }
        });
        
        document.addEventListener('mousedown', function() {
            document.body.classList.remove('keyboard-navigation');
        });
    }
});



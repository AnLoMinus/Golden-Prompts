document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('prompt-form');
    const resultSection = document.getElementById('result-section');
    const resultPre = document.getElementById('result');
    const copyButton = document.getElementById('copy-button');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const context = document.getElementById('context').value;
        const role = document.getElementById('role').value;
        const task = document.getElementById('task').value;
        const constraints = document.getElementById('constraints').value;
        const format = document.getElementById('format').value;
        const style = document.getElementById('style').value;
        const length = document.getElementById('length').value;
        const examples = document.getElementById('examples').value;
        const customParameters = document.getElementById('custom-parameters').value;

        const prompt = {
            context: context,
            role: role,
            task: task,
            constraints: constraints.split('\n').filter(x => x.trim() !== ''),
            format: format,
            style: style,
            length: length,
            examples: examples.split('\n').filter(x => x.trim() !== ''),
            custom_parameters: customParameters.split('\n').filter(x => x.trim() !== '')
        };

        resultPre.textContent = JSON.stringify(prompt, null, 2);
        resultSection.style.display = 'block';
    });

    copyButton.addEventListener('click', function() {
        navigator.clipboard.writeText(resultPre.textContent)
            .then(() => {
                alert('Prompt copied to clipboard!');
            })
            .catch(err => {
                alert('Failed to copy prompt: ' + err);
            });
    });
});
const container = document.getElementById('container-with-shadow-dom');
const shadowRoot = container.attachShadow({ mode: 'open' });

shadowRoot.innerHTML = `
    <style>
        button {
            background-color: blue;
            color: white;
            padding: 10px;
            border: none;
            cursor: pointer;
        }
    </style>
    <button>Click me</button>
    <slot></slot>
`;

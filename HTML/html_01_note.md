#  ::before  ::selection
    <style>

        a::before {
            content: "\21d2 Click Here: ";
            font-weight: bold;
        }

        p::selection {
            color: green;
            background-color: darkslategray;

    </style>

# selectors

    No need to remember, read documentation

    a, b, c  ~  multiple elements
    a b      ~  decendant selector
    a > b    ~  child selector
    a + b    ~  adjacent sibling
    [a=b]    ~  attribute selector
    a:b      ~  pseudoclass
    a::b     ~  pseudoelement

# Responsive Design
    viewport
    media query
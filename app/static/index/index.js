document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("#create-blank-form").addEventListener("click", () => {
        const csrf = Cookies.get('csrftoken');
        fetch('/forms/form/create', {
            method: "POST",
            headers: {'X-CSRFToken': csrf},
            body: JSON.stringify({
                title: "Untitled Form"
            })
        })
        .then(response => response.json())
        .then(result => {
            window.location = `/forms/form/${result.code}/edit`
        })
    })
    document.querySelector("#create-contact-form").addEventListener("click", () => {
        const csrf = Cookies.get('csrftoken');
        fetch('/forms/form/create/contact', {
            method: "POST",
            headers: {'X-CSRFToken': csrf},
            body: JSON.stringify({})
        })
        .then(response => response.json())
        .then(result => {
            window.location = `/forms/form/${result.code}/edit`
        })
    })
    document.querySelector("#create-customer-feedback").addEventListener("click", () => {
        const csrf = Cookies.get('csrftoken');
        fetch('/forms/form/create/feedback', {
            method: "POST",
            headers: {'X-CSRFToken': csrf},
            body: JSON.stringify({})
        })
        .then(response => response.json())
        .then(result => {
            window.location = `/forms/form/${result.code}/edit`
        })
    })
    document.querySelector("#create-event-registration").addEventListener("click", () => {
        const csrf = Cookies.get('csrftoken');
        fetch('/forms/form/create/event', {
            method: "POST",
            headers: {'X-CSRFToken': csrf},
            body: JSON.stringify({})
        })
        .then(response => response.json())
        .then(result => {
            window.location = `/forms/form/${result.code}/edit`
        })
    })
})
// get values from user form fields

const sendToServer = (url, formData) => {
    const data = Object.fromEntries(formData.entries());
    let options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    };
    return new Promise((resolve, reject) => {
        fetch(url, options)
            .then((resp) => resp.json())
            .then((res) => resolve(res))
            .catch((err) => reject(err));
    });
};

const handleFormSubmit = (e) => {
    e.preventDefault();
    console.log("form submitted");

    const form = e.currentTarget;
    const url = "http://127.0.0.1:8000/api/mail/save_user/";
    try {
        const formData = new FormData(form);
        // console.log(formData,formData.entries(),Object.fromEntries(formData.entries()))
        sendToServer(url, formData)
            .then((res) => {
                console.log("response", res);
                createAlert('success',res.msg);
            })
            .catch((err) => {
                console.log("error", err)
                createAlert("danger","unable to save your query. Try again!")
            });
    } catch (err) {
        console.log(err);
    }
};

function createAlert(type, message) {
    const alert_container = document.getElementById("alert_container");
    let alert_item = `<div class="alert alert-${
        type ? type : "warning"
    } alert-dismissible fade show" role="alert">
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>`;

    alert_container.innerHTML = alert_item;
}

// adding submit event listener to form node
const formNode = document.getElementById("contact_us_form");
formNode.addEventListener("submit", handleFormSubmit);

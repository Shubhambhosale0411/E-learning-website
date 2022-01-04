console.log("Script Connected");

function show_modal(e) {
    // console.log(e,e.currentTarget.getAttribute('data-content'))
    const modal_body = document.querySelector(
        "#avatarModal .modal-body .short_summary"
    );
    const modal_title = document.querySelector(
        "#avatarModal #avatarModalLabel"
    );
    const modal_main_content = document.querySelector(
        "#avatarModal .modal-body #avatar_main_content"
    );

    const data_short_content =
        e.currentTarget.getAttribute("data-shortContent");
    const data_long_content = e.currentTarget.getAttribute("data-content");
    const data_title = e.currentTarget.getAttribute("data-title");

    modal_body.innerText = data_short_content
        ? data_short_content
        : modal_body.innerText;
    modal_title.innerText = data_title ? data_title : modal_title.innerText;
    modal_main_content.innerText = data_long_content;

    modalRef.show();
}

function toggle_know_more() {
    let collapseEl = document.getElementById("avatar_main_content");
    var collapseRef = new bootstrap.Collapse(collapseEl);
    collapseRef.toggle();
}

////===== carousel config
var myCarousel = document.querySelector("#backgroundImageCarousel");
var carousel = new bootstrap.Carousel(myCarousel, {
    interval: 2000,
    wrap: true,
});
// End

////===== dynamically change content of avatar modals
var myModal = document.getElementById("avatarModal");
var modalRef = new bootstrap.Modal(myModal, {
    keyboard: false,
});

// main content to be shown onknow more click button
let collapseEl = document.getElementById("avatar_main_content");
var collapseRef = new bootstrap.Collapse(collapseEl);

// close know more content on modal close
myModal.addEventListener("hidden.bs.modal", function () {
    collapseRef.hide();
});

collapseEl.addEventListener("hidden.bs.collapse", function () {
    console.log("know more hidden");
});

// setting up click event listener
const avatar_cards = document.getElementsByClassName("avatar_card");

for (let avatar_card of avatar_cards)
    avatar_card.addEventListener("click", show_modal);

// End

// track for click events on know more button to open extra content
const btn_know_more = document.getElementById("btn_know_more");
btn_know_more.addEventListener("click", toggle_know_more);

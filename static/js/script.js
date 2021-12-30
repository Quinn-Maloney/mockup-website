document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("conferenceId").addEventListener("change", getCookie);
    document.getElementById("1").addEventListener("change", vote());
    document.getElementById("2").addEventListener("change", vote());
    document.getElementById("3").addEventListener("change", vote());
    document.addEventListener("DOMContentLoaded", getLocalStorage());
});

function openMessage() {
    var getText;

    if(document.getElementById('1').checked){
        getText = document.getElementById('1').value;
    }
    else if(document.getElementById('2').checked){
        getText = document.getElementById('2').value;
    }
    else if(document.getElementById('3').checked) {
        getText = document.getElementById('3').value;
    }
    //var getText = document.getElementById('message');
    window.alert(`Thank you for voting for ` + getText);

}

function registrationRestriction() {
    var a = document.getElementById('A');
    var b = document.getElementById('B');
    var c = document.getElementById('C');
    var d = document.getElementById('D');
    var e = document.getElementById('E');
    var f = document.getElementById('F');
    var g = document.getElementById('G');
    var h = document.getElementById('H');
    var i = document.getElementById('I');

    if(b.checked) {
        d.disabled = true;
        e.disabled = true;
        f.disabled = true;
        h.disabled = true;
        alert("If registering for the drowning process and how to rescue a guest in distress workshop, " +
            "you cannot register for any workshops in Session 2, or the workshop labeled " +
            "The Types of Burns and How to Treat Them.")
    } else {
        d.disabled = false;
        e.disabled = false;
        f.disabled = false;
        h.disabled = false;
    }
    if(f.checked) {
        g.disabled = true;
        i.disabled = true;
        //must select H
        h.checked = true;
        alert("If registering for choking and obstructed airway scenarios workshop, " +
            "you must also register for the types of burns and how to treat them workshop.")
    } else {
        g.disabled = false;
        i.disabled = false;
        h.checked = false;
        //cannot take H
        h.disabled = true;
    }
}

function validationMessage() {
    var newWindow = window.open("", null, "height=400,width=500,status=yes,toolbar=no,menubar=no,location=no");
    if(b.checked && (d.checked || e.checked || f.checked || h.checked)) {
        newWindow.document.write("ERROR: If attending the second workshop in session 1, no workshop in " +
            "session 2 may be selected.");
    }
    if(f.checked && (g.checked || i.checked)) {
        newWindow.document.write("ERROR: If attending the last workshop in session 2, the first " +
            "and last workshops in session 3 may not be selected.");
    }
    if(f.checked && (!h.checked)) {
        newWindow.document.write("ERROR: If attending the last workshop in session 2, the " +
            "second workshop in session 3 must be selected.");
    }
    if(!f.checked && h.checked) {
        newWindow.document.write("ERROR: The last workshop in session 2 must be taken with " +
            "the second workshop in session 3.");
    }
}
//
function setCookie() {
    //if submitted, open thank you page
    let submit = document.getElementById('submitValue');
    let name = document.getElementById('name')
    if(submit.checked) {
        window.open("thankyou.html")
    }

    //const fields = ["conferenceId", "name", "address", "city1", "state1", "zip1", "email", "tel", "companyName", "position", "url", "group1", "group2", "group3"];
    //fields.forEach(v => document.cookie = `${v}=${document.getElementById(v).value};`);



}

// retrieve cookie info

function getCookie() {
    let enteredId = document.getElementById("conferenceId").value;
    let cookieFields = document.cookie.split(';').map(v => v.trim());
    let userId = cookieFields.find(v=> v.startsWith("conferenceId")).split("=")[1];
    console.log("it work");
    if(userId == enteredId) {
        cookieFields.map(v => v.split("=")).forEach(([k, v]) => document.getElementById(k).innerHTML =v);

    }

}

//local storage
function vote() {
    if(!Number(localStorage.getItem("1"))) {
        let entry1Votes = 0;
        //set span value on the DOM
    }
    else {
        let entry1Votes = Number(localStorage.getItem("1"));
    }
    if(!Number(localStorage.getItem("2"))){
        let entry2Votes = 0;
    }
    else {
        let entry2Votes = Number(localStorage.getItem("2"));
    }
    if(!Number(localStorage.getItem("3"))) {
        let entry3Votes = 0;
    }
    else {
        let entry3Votes = Number(localStorage.getItem("3"));
    }

    if(document.getElementById("1").checked) {
        entry1Votes++;
    }
    else if(document.getElementById("2").checked) {
        entry2Votes++;
    }
    else if(document.getElementById("3").checked){
        entry3Votes++;
    }

    localStorage.setItem("1", entry1Votes);
    localStorage.setItem("2", entry2Votes);
    localStorage.setItem("3", entry3Votes);
}

function getLocalStorage() {
    let count1 = Number(localStorage.getItem("1"));
    let count2 = Number(localStorage.getItem("2"));
    let count3 = Number(localStorage.getItem("3"));

    window.alert("Entry 1 total votes = " + count1 + '\n' +
    "Entry 2 total votes = " + count2 + '\n' +
        "Entry 3 total votes = " + count3);
}

//awards page poll
function awardsVote() {
    if(op1.checked) {
        alert("Thank you for voting for Image 1!")
    }
    else if(op2.checked) {
        alert("Thank you for voting for Image 2!")
    }
    else if(op3.checked) {
        alert("Thank you for voting for Image 3!")
    }

}


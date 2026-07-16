const API_URL = "https://g5sqrlfzu3.execute-api.ap-south-1.amazonaws.com";

const notesList = document.getElementById("notesList");
const noteContent = document.getElementById("noteContent");
const toast = document.getElementById("toast");

function showToast(message, success = true) {
    toast.innerHTML = message;
    toast.style.display = "block";
    toast.style.background = success ? "#16a34a" : "#dc2626";

    setTimeout(() => {
        toast.style.display = "none";
    }, 3000);
}

async function saveNote() {

    const filename = document.getElementById("filename").value.trim();
    const content = document.getElementById("content").value.trim();

    if (!filename || !content) {
        showToast("Please enter filename and content.", false);
        return;
    }

    try {

        const response = await fetch(`${API_URL}/note`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                filename,
                content
            })

        });

        const result = await response.json();

        if (response.ok) {

            showToast(result.message);

            document.getElementById("filename").value = "";
            document.getElementById("content").value = "";

            loadNotes();

        } else {

            showToast(result.error || "Failed to save note.", false);

        }

    } catch (err) {

        console.error(err);

        showToast("Network Error", false);

    }

}

async function loadNotes() {

    notesList.innerHTML = "<p style='color:white;'>Loading...</p>";

    try {

        const response = await fetch(`${API_URL}/notes`);

        const result = await response.json();

        notesList.innerHTML = "";

        if (!result.notes || result.notes.length === 0) {

            notesList.innerHTML = "<p style='color:white;'>No notes available.</p>";
            return;

        }

        result.notes.forEach(note => {

            const card = document.createElement("div");

            card.className = "note-card";

            card.innerHTML = `
                <h4>${note}</h4>
                <p>Click to view</p>
            `;

            card.onclick = () => loadNote(note);

            notesList.appendChild(card);

        });

    } catch (err) {

        console.error(err);

        showToast("Unable to load notes.", false);

    }

}

async function loadNote(filename) {

    try {

        const response = await fetch(`${API_URL}/note?filename=${encodeURIComponent(filename)}`);

        const result = await response.json();

        noteContent.textContent = result.content;

    } catch (err) {

        console.error(err);

        showToast("Unable to load note.", false);

    }

}

window.onload = () => {
    loadNotes();
};
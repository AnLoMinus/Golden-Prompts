document.addEventListener("DOMContentLoaded", function () {
  const profiles = [];

  // Profile Management Functions
  function createProfile() {
    const name = document.getElementById("profileName").value;
    const description = document.getElementById("profileDescription").value;
    const tone = document.getElementById("profileTone").value;
    const formality = document.getElementById("profileFormality").value;
    const interests = document.getElementById("profileInterests").value;

    if (!name) {
      alert("נא הכנס שם לפרופיל");
      return;
    }

    const profile = { name, description, tone, formality, interests };
    profiles.push(profile);
    updateProfileList();
    clearProfileForm();
  }

  function updateProfileList() {
    const profileList = document.getElementById("profileList");
    profileList.innerHTML = "";
    profiles.forEach((profile, index) => {
      const listItem = document.createElement("li");
      listItem.textContent = `${profile.name} - ${profile.description}`;
      const editButton = document.createElement("button");
      editButton.textContent = "ערוך";
      editButton.onclick = () => editProfile(index);
      const deleteButton = document.createElement("button");
      deleteButton.textContent = "מחק";
      deleteButton.onclick = () => deleteProfile(index);
      listItem.appendChild(editButton);
      listItem.appendChild(deleteButton);
      profileList.appendChild(listItem);
    });
  }

  function editProfile(index) {
    const profile = profiles[index];
    document.getElementById("profileName").value = profile.name;
    document.getElementById("profileDescription").value = profile.description;
    document.getElementById("profileTone").value = profile.tone;
    document.getElementById("profileFormality").value = profile.formality;
    document.getElementById("profileInterests").value = profile.interests;
    profiles.splice(index, 1); // Remove the profile to allow for re-creation
    updateProfileList();
  }

  function deleteProfile(index) {
    if (confirm("האם אתה בטוח שברצונך למחוק את הפרופיל הזה?")) {
      profiles.splice(index, 1);
      updateProfileList();
    }
  }

  function clearProfileForm() {
    document.getElementById("profileName").value = "";
    document.getElementById("profileDescription").value = "";
    document.getElementById("profileTone").value = "formal";
    document.getElementById("profileFormality").value = "formal";
    document.getElementById("profileInterests").value = "";
  }

  // Prompt Management Functions
  function generatePrompt() {
    // Placeholder for generating prompt functionality
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "<p>פקודה נוצרה!</p>"; // Example result
  }

  function exportPrompt() {
    // Placeholder for exporting prompt functionality
    alert("הפקודה ייצאה!");
  }

  function saveTemplate() {
    // Placeholder for saving template functionality
    alert("התבנית נשמרה!");
  }

  function loadTemplate() {
    // Placeholder for loading template functionality
    alert("התבנית נטענה!");
  }

  function clearForm() {
    document.getElementById("prompt-form").reset();
  }

  function previewPrompt() {
    // Placeholder for previewing prompt functionality
    alert("תצוגה מקדימה של הפקודה");
  }

  function copyToClipboard() {
    // Placeholder for copying prompt to clipboard functionality
    alert("הפקודה הועתקה ללוח!");
  }

  function printPrompt() {
    // Placeholder for printing prompt functionality
    alert("הפקודה הודפסה!");
  }

  function sharePrompt() {
    // Placeholder for sharing prompt functionality
    alert("הפקודה שותפה!");
  }

  function saveAsTemplate() {
    // Placeholder for saving as template functionality
    alert("נשמר כתבנית!");
  }

  function loadFromFile() {
    // Placeholder for loading from file functionality
    alert("טען מקובץ!");
  }

  function clearResults() {
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "";
  }

  // Settings Functions
  function changeFontSize() {
    const fontSize = document.getElementById("fontSize").value;
    document.body.style.fontSize = fontSize;
  }

  function changeLanguage() {
    const language = document.getElementById("languageSetting").value;
    // Implement language change logic here
    alert(`שפה שונתה ל-${language}`);
  }

  function resetFields() {
    clearProfileForm();
    clearForm();
    clearResults();
    // Implement additional field reset logic if needed
  }

  function toggleNotifications() {
    // Placeholder for toggling notifications functionality
    alert("התראות הופעלו/כובו!");
  }

  function toggleAutoSave() {
    // Placeholder for toggling auto-save functionality
    alert("שמירה אוטומטית הופעלה/כובתה!");
  }

  function exportSettings() {
    // Placeholder for exporting settings functionality
    alert("הגדרות ייצאו!");
  }

  function importSettings() {
    // Placeholder for importing settings functionality
    alert("הגדרות יובאו!");
  }

  // Event Listeners
  document
    .getElementById("theme-toggle")
    .addEventListener("click", function () {
      document.body.classList.toggle("dark-mode");
    });

  document
    .getElementById("toggle-display")
    .addEventListener("click", function () {
      const sections = document.querySelectorAll(".section");
      sections.forEach((section) => {
        section.classList.toggle("active");
      });
    });

  document
    .getElementById("reset-settings")
    .addEventListener("click", resetFields);

  document
    .querySelector("#profile-form button")
    .addEventListener("click", createProfile);

  document
    .querySelector('#prompt-form button[onclick="generatePrompt()"]')
    .addEventListener("click", generatePrompt);
  document
    .querySelector('#prompt-form button[onclick="exportPrompt()"]')
    .addEventListener("click", exportPrompt);
  document
    .querySelector('#prompt-form button[onclick="saveTemplate()"]')
    .addEventListener("click", saveTemplate);
  document
    .querySelector('#prompt-form button[onclick="loadTemplate()"]')
    .addEventListener("click", loadTemplate);
  document
    .querySelector('#prompt-form button[onclick="clearForm()"]')
    .addEventListener("click", clearForm);
  document
    .querySelector('#prompt-form button[onclick="previewPrompt()"]')
    .addEventListener("click", previewPrompt);
  document
    .querySelector('#prompt-form button[onclick="copyToClipboard()"]')
    .addEventListener("click", copyToClipboard);
  document
    .querySelector('#prompt-form button[onclick="printPrompt()"]')
    .addEventListener("click", printPrompt);
  document
    .querySelector('#prompt-form button[onclick="sharePrompt()"]')
    .addEventListener("click", sharePrompt);
  document
    .querySelector('#prompt-form button[onclick="saveAsTemplate()"]')
    .addEventListener("click", saveAsTemplate);
  document
    .querySelector('#prompt-form button[onclick="loadFromFile()"]')
    .addEventListener("click", loadFromFile);

  document
    .querySelector("#result-section button")
    .addEventListener("click", clearResults);

  document
    .querySelector("#settings-section #fontSize")
    .addEventListener("change", changeFontSize);
  document
    .querySelector("#settings-section #languageSetting")
    .addEventListener("change", changeLanguage);
  document
    .querySelector('#settings-section button[onclick="resetFields()"]')
    .addEventListener("click", resetFields);
  document
    .querySelector('#settings-section button[onclick="toggleNotifications()"]')
    .addEventListener("click", toggleNotifications);
  document
    .querySelector('#settings-section button[onclick="toggleAutoSave()"]')
    .addEventListener("click", toggleAutoSave);
  document
    .querySelector('#settings-section button[onclick="exportSettings()"]')
    .addEventListener("click", exportSettings);
  document
    .querySelector('#settings-section button[onclick="importSettings()"]')
    .addEventListener("click", importSettings);
});

function changeWindowWidth() {
  const width = document.getElementById("windowWidth").value;
  document.querySelectorAll(".section").forEach((section) => {
    section.style.width = width;
  });
}

function changeWindowHeight() {
  const height = document.getElementById("windowHeight").value;
  document.querySelectorAll(".section").forEach((section) => {
    section.style.height = height;
  });
}

function changeItemsPerPage() {
  const itemsPerPage = document.getElementById("itemsPerPage").value;
  // כאן תוכל להוסיף קוד למיון ושינוי כמות הצגה
}

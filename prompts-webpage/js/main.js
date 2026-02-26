document.addEventListener("DOMContentLoaded", () => {
  // Auto-translation setup
  function setupAutoTranslation() {
    // Get user's browser language (first 2 chars only - language code)
    const userLang = navigator.language || navigator.userLanguage;
    const langCode = userLang.split("-")[0];

    // If language is not English, initialize Google Translate
    if (langCode !== "en") {
      const script = document.createElement("script");
      script.src =
        "//translate.google.com/translate_a/element.js?cb=initGoogleTranslate";
      document.head.appendChild(script);

      // Add Google Translate meta tag
      const meta = document.createElement("meta");
      meta.name = "google";
      meta.content = "notranslate";
      document.head.appendChild(meta);
    }
  }

  // Google Translate initialization function
  window.initGoogleTranslate = function () {
    new google.translate.TranslateElement(
      {
        pageLanguage: "en",
        autoDisplay: true,
        includedLanguages: "", // Empty string means all languages
        layout: google.translate.TranslateElement.InlineLayout.SIMPLE,
      },
      "google_translate_element"
    );

    // Hide Google Translate widget after initialization
    const translateWidget = document.querySelector(".goog-te-gadget");
    if (translateWidget) {
      translateWidget.style.display = "none";
    }

    // Auto-trigger translation to user's language
    const userLang = navigator.language || navigator.userLanguage;
    const langCode = userLang.split("-")[0];
    if (langCode !== "en") {
      const translateCombo = document.querySelector(".goog-te-combo");
      if (translateCombo) {
        translateCombo.value = langCode;
        translateCombo.dispatchEvent(new Event("change"));
      }
    }
  };

  // Initialize auto-translation
  setupAutoTranslation();

  const toggleBtn = document.getElementById("toggleSidebar");
  const sidebar = document.querySelector(".sidebar");
  const searchInput = document.getElementById("searchInput");
  const searchBtn = document.getElementById("searchBtn");
  const promptsContainer = document.getElementById("promptsContainer");
  const categoryList = document.getElementById("categoryList");
  const sortSelect = document.getElementById("sortSelect");
  const gridViewBtn = document.getElementById("gridView");
  const listViewBtn = document.getElementById("listView");
  const activeFilters = document.getElementById("activeFilters");

  let activeCategories = new Set();
  let currentView = "grid";
  let currentSort = "titleAsc";
  let searchQuery = "";

  // Toggle sidebar
  toggleBtn.addEventListener("click", () => {
    sidebar.classList.toggle("active");
  });

  // Add emoji mapping for categories
  const categoryEmojis = {
    "Blog Writing": "📝",
    "SEO Optimization": "🎯",
    "Content Optimization": "⚡",
    Branding: "™️",
    "Technical Writing": "📚",
    Marketing: "📢",
    "Product Documentation": "📋",
    "Web Development": "💻",
    "Case Studies": "📊",
    "Future Trends": "🔮",
    Educational: "🎓",
    Resources: "🛠️",
    Glossary: "📖",
    "Q&A": "❓",
    Infographics: "📈",
    "Quick Guides": "⚡",
    "Advanced Guides": "🚀",
    "Expert Guides": "👨‍💻",
    "Expert Tips": "💡",
    "Comparative Analysis": "⚖️",
    Trends: "📊",
    "Historical Analysis": "📜",
    "Drawing Prompts": "🎨",
    "Task Management": "✅",
    "Service Pages": "🔧",
  };

  // Generate categories
  const categories = [
    ...new Set(prompts.map((prompt) => prompt.category)),
  ].sort();
  categories.forEach((category) => {
    const li = document.createElement("li");
    const emoji = categoryEmojis[category] || "📌"; // Default emoji if category not found
    li.innerHTML = `${emoji} ${category}`;
    li.addEventListener("click", () => toggleCategory(category));
    categoryList.appendChild(li);
  });

  // Toggle category filter
  function toggleCategory(category) {
    if (activeCategories.has(category)) {
      activeCategories.delete(category);
    } else {
      activeCategories.add(category);
    }
    updateActiveFilters();
    filterAndDisplayPrompts();
  }

  // Update active filters display with emojis
  function updateActiveFilters() {
    activeFilters.innerHTML = "";
    activeCategories.forEach((category) => {
      const tag = document.createElement("span");
      tag.className = "filter-tag";
      const emoji = categoryEmojis[category] || "📌";
      tag.innerHTML = `
                ${emoji} ${category}
                <button onclick="removeCategory('${category}')">
                    <i class="fas fa-times"></i>
                </button>
            `;
      activeFilters.appendChild(tag);
    });
  }

  // Remove category filter
  window.removeCategory = function (category) {
    activeCategories.delete(category);
    updateActiveFilters();
    filterAndDisplayPrompts();
  };

  // Sort prompts
  function sortPrompts(prompts) {
    return prompts.sort((a, b) => {
      switch (currentSort) {
        case "titleAsc":
          return a.title.localeCompare(b.title);
        case "titleDesc":
          return b.title.localeCompare(a.title);
        case "categoryAsc":
          return a.category.localeCompare(b.category);
        case "categoryDesc":
          return b.category.localeCompare(a.category);
        default:
          return 0;
      }
    });
  }

  // Filter and display prompts
  function filterAndDisplayPrompts() {
    let filtered = prompts;

    // Apply category filters
    if (activeCategories.size > 0) {
      filtered = filtered.filter((prompt) =>
        activeCategories.has(prompt.category)
      );
    }

    // Apply search filter
    if (searchQuery) {
      filtered = filtered.filter(
        (prompt) =>
          prompt.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
          prompt.content.toLowerCase().includes(searchQuery.toLowerCase()) ||
          prompt.category.toLowerCase().includes(searchQuery.toLowerCase())
      );
    }

    // Sort filtered prompts
    filtered = sortPrompts(filtered);

    // Display filtered prompts
    displayPrompts(filtered);
  }

  // Display prompts
  function displayPrompts(promptsToShow) {
    promptsContainer.innerHTML = "";
    promptsToShow.forEach((prompt, index) => {
      const card = document.createElement("div");
      card.className = "prompt-card";

      card.innerHTML = `
          <div class="card-header">
              <h3 class="prompt-title">${prompt.title}</h3>
              <div class="card-actions">
                  <button class="settings-btn" onclick="openPromptSettings(${index})" data-tooltip="Configure Prompt">
                      <i class="fas fa-cog"></i>
                  </button>
                  <button class="copy-btn" onclick="copyPrompt(this)" data-tooltip="Copy Prompt">
                      <i class="fas fa-copy"></i>
                  </button>
              </div>
          </div>
          <span class="prompt-category">${prompt.category}</span>
          <p class="prompt-content">${prompt.content}</p>
      `;
      promptsContainer.appendChild(card);
    });
  }

  // Event Listeners
  searchBtn.addEventListener("click", () => {
    searchQuery = searchInput.value;
    filterAndDisplayPrompts();
  });

  searchInput.addEventListener("keyup", (e) => {
    if (e.key === "Enter") {
      searchQuery = searchInput.value;
      filterAndDisplayPrompts();
    }
  });

  sortSelect.addEventListener("change", (e) => {
    currentSort = e.target.value;
    filterAndDisplayPrompts();
  });

  gridViewBtn.addEventListener("click", () => {
    currentView = "grid";
    promptsContainer.className = "prompts-container grid-view";
    gridViewBtn.classList.add("active");
    listViewBtn.classList.remove("active");
  });

  listViewBtn.addEventListener("click", () => {
    currentView = "list";
    promptsContainer.className = "prompts-container list-view";
    listViewBtn.classList.add("active");
    gridViewBtn.classList.remove("active");
  });

  // Topic Form Handling
  const topicForm = document.getElementById("topicForm");
  let currentTopicConfig = {
    name: "",
    description: "",
    industry: "",
  };

  topicForm.addEventListener("submit", (e) => {
    e.preventDefault();
    currentTopicConfig = {
      name: document.getElementById("topicName").value,
      description: document.getElementById("topicDescription").value,
      industry: document.getElementById("industry").value,
    };
    filterAndDisplayPrompts();
    modal.classList.remove("active"); // Close modal after submission
  });

  // Copy functionality
  window.copyPrompt = function (button) {
    const card = button.closest(".prompt-card");
    const content = card.querySelector(".prompt-content").textContent;

    navigator.clipboard.writeText(content).then(() => {
      // Show success message
      const message = document.createElement("div");
      message.className = "copy-success";
      message.textContent = "Copied to clipboard!";
      document.body.appendChild(message);

      // Remove message after animation
      setTimeout(() => {
        message.remove();
      }, 2000);
    });
  };

  // Initial display
  filterAndDisplayPrompts();

  // Modal functionality
  const configureTopicBtn = document.getElementById("configureTopicBtn");
  const modal = document.getElementById("topicFormModal");
  const closeModal = document.querySelector(".close-modal");

  configureTopicBtn.addEventListener("click", () => {
    modal.classList.add("active");
  });

  closeModal.addEventListener("click", () => {
    modal.classList.remove("active");
  });

  // Close modal when clicking outside
  modal.addEventListener("click", (e) => {
    if (e.target === modal) {
      modal.classList.remove("active");
    }
  });

  // Add keyboard shortcuts
  document.addEventListener("keydown", (e) => {
    // Ctrl/Cmd + K to focus search
    if ((e.ctrlKey || e.metaKey) && e.key === "k") {
      e.preventDefault();
      searchInput.focus();
    }

    // Esc to close modal
    if (e.key === "Escape" && modal.classList.contains("active")) {
      modal.classList.remove("active");
    }

    // Ctrl/Cmd + / to toggle dark mode
    if ((e.ctrlKey || e.metaKey) && e.key === "/") {
      e.preventDefault();
      document.body.classList.toggle("dark-mode");
    }
  });

  // Add favorites functionality
  function toggleFavorite(promptId) {
    let favorites = JSON.parse(localStorage.getItem("favorites") || "[]");

    if (favorites.includes(promptId)) {
      favorites = favorites.filter((id) => id !== promptId);
    } else {
      favorites.push(promptId);
    }

    localStorage.setItem("favorites", JSON.stringify(favorites));
    updateFavoriteButtons();
  }

  function updateFavoriteButtons() {
    const favorites = JSON.parse(localStorage.getItem("favorites") || "[]");
    document.querySelectorAll(".favorite-btn").forEach((btn) => {
      const promptId = btn.dataset.promptId;
      btn.classList.toggle("active", favorites.includes(promptId));
    });
  }

  // Info Modal functionality
  const infoBtn = document.getElementById("infoBtn");
  const infoModal = document.getElementById("infoModal");
  const tabBtns = document.querySelectorAll(".tab-btn");
  const tabContents = document.querySelectorAll(".tab-content");

  infoBtn.addEventListener("click", () => {
    infoModal.classList.add("active");
  });

  // Tab functionality
  tabBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      // Remove active class from all buttons and contents
      tabBtns.forEach((b) => b.classList.remove("active"));
      tabContents.forEach((c) => c.classList.remove("active"));

      // Add active class to clicked button and corresponding content
      btn.classList.add("active");
      document.getElementById(btn.dataset.tab).classList.add("active");
    });
  });

  // Close info modal when clicking outside
  infoModal.addEventListener("click", (e) => {
    if (e.target === infoModal) {
      infoModal.classList.remove("active");
    }
  });

  // Close info modal with escape key
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && infoModal.classList.contains("active")) {
      infoModal.classList.remove("active");
    }
  });

  // Add new functions for prompt settings
  window.openPromptSettings = function (promptIndex) {
    const prompt = prompts[promptIndex];
    const modal = document.createElement("div");
    modal.className = "modal prompt-settings-modal";
    modal.innerHTML = `
        <div class="modal-content">
            <div class="modal-header">
                <h3>Configure Prompt: ${prompt.title}</h3>
                <button class="close-modal" onclick="closePromptSettings(this)">&times;</button>
            </div>
            <div class="modal-body">
                <form id="promptSettingsForm-${promptIndex}" class="prompt-settings-form">
                    <div class="form-group">
                        <label>Topic/Term Name:</label>
                        <input type="text" class="topic-input" placeholder="Enter topic" 
                               oninput="updatePreview(${promptIndex})">
                    </div>
                    <div class="form-group">
                        <label>Current Year:</label>
                        <input type="number" class="year-input" value="${new Date().getFullYear()}"
                               oninput="updatePreview(${promptIndex})">
                    </div>
                    <div class="preview-section">
                        <h4>Preview</h4>
                        <div class="preview-content"></div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="modal-btn secondary" onclick="resetPromptSettings(${promptIndex})">
                            Reset
                        </button>
                        <button type="button" class="modal-btn primary" onclick="copyConfiguredPrompt(${promptIndex})">
                            Apply & Copy
                        </button>
                    </div>
                </form>
            </div>
        </div>
    `;
    document.body.appendChild(modal);
    setTimeout(() => modal.classList.add("active"), 10);
    updatePreview(promptIndex);
  };

  window.updatePreview = function (promptIndex) {
    const form = document.getElementById(`promptSettingsForm-${promptIndex}`);
    const preview = form.querySelector(".preview-content");
    const prompt = prompts[promptIndex];
    const topic = form.querySelector(".topic-input").value;
    const year = form.querySelector(".year-input").value;

    let content = prompt.content
      .replace(/\[Topic\]/g, topic || "[Topic]")
      .replace(/\[Term\]/g, topic || "[Term]")
      .replace(/{put-here-topic}/g, topic || "{put-here-topic}")
      .replace(/\[Current Year\]/g, year);

    preview.innerHTML = `<div class="preview-card">${content}</div>`;
  };

  window.copyConfiguredPrompt = function (promptIndex) {
    const form = document.getElementById(`promptSettingsForm-${promptIndex}`);
    const preview = form.querySelector(".preview-content").textContent;

    navigator.clipboard.writeText(preview).then(() => {
      showSuccessMessage("Configured prompt copied to clipboard!");
      closePromptSettings(form.querySelector(".close-modal"));
    });
  };

  window.resetPromptSettings = function (promptIndex) {
    const form = document.getElementById(`promptSettingsForm-${promptIndex}`);
    form.reset();
    updatePreview(promptIndex);
  };

  window.closePromptSettings = function (button) {
    const modal = button.closest(".modal");
    modal.classList.remove("active");
    setTimeout(() => modal.remove(), 300);
  };

  function showSuccessMessage(message) {
    const messageEl = document.createElement("div");
    messageEl.className = "copy-success";
    messageEl.textContent = message;
    document.body.appendChild(messageEl);
    setTimeout(() => messageEl.remove(), 2000);
  }

  // Update the info modal close functionality
  const infoModalCloseBtn = document.querySelector("#infoModal .close-modal");
  infoModalCloseBtn.addEventListener("click", () => {
    infoModal.classList.remove("active");
  });
});

document.addEventListener("DOMContentLoaded", () => {
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
    promptsToShow.forEach((prompt) => {
      const card = document.createElement("div");
      card.className = "prompt-card";

      // Replace [Topic] and other placeholders with actual values
      let processedContent = prompt.content
        .replace(/\[Topic\]/g, currentTopicConfig.name)
        .replace(/\[Term\]/g, currentTopicConfig.name)
        .replace(/{put-here-topic}/g, currentTopicConfig.name);

      let processedTitle = prompt.title
        .replace(/\[Topic\]/g, currentTopicConfig.name)
        .replace(/\[Term\]/g, currentTopicConfig.name);

      card.innerHTML = `
          <h3 class="prompt-title">${processedTitle}</h3>
          <span class="prompt-category">${prompt.category}</span>
          <p class="prompt-content">${processedContent}</p>
          <button class="copy-btn" onclick="copyPrompt(this)">
              <i class="fas fa-copy"></i>
          </button>
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
});

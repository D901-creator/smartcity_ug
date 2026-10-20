(function () {
    "use strict";

    const header = document.getElementById("siteHeader");
    const languageSelect = document.getElementById("languageSelect");
    const languageElements = document.querySelectorAll("[data-en][data-lg]");

    function applyLanguage(language) {
        const selectedLanguage = language === "lg" ? "lg" : "en";

        document.documentElement.lang = selectedLanguage === "lg" ? "lg" : "en";

        languageElements.forEach(function (element) {
            const translatedText = element.getAttribute(
                selectedLanguage === "lg" ? "data-lg" : "data-en"
            );

            if (translatedText !== null) {
                // The bilingual headings intentionally contain inline <span> styling.
                if (element.querySelector("span") &&
                    /<span>/.test(translatedText)) {
                    element.innerHTML = translatedText;
                } else {
                    element.textContent = translatedText;
                }
            }
        });

        if (languageSelect) {
            languageSelect.value = selectedLanguage;
        }

        try {
            sessionStorage.setItem("smartCityLanguage", selectedLanguage);
        } catch (error) {
            // The page still works if browser storage is unavailable.
        }
    }

    if (languageSelect) {
        languageSelect.addEventListener("change", function () {
            applyLanguage(languageSelect.value);
        });
    }

    try {
        const savedLanguage = sessionStorage.getItem("smartCityLanguage");
        if (savedLanguage) {
            applyLanguage(savedLanguage);
        }
    } catch (error) {
        // Default language remains English.
    }

    function updateHeader() {
        if (header) {
            header.classList.toggle("scrolled", window.scrollY > 12);
        }
    }

    window.addEventListener("scroll", updateHeader, { passive: true });
    updateHeader();

    const revealElements = document.querySelectorAll(".reveal");

    if ("IntersectionObserver" in window) {
        const observer = new IntersectionObserver(function (entries, currentObserver) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add("visible");
                    currentObserver.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.12,
            rootMargin: "0px 0px -30px 0px"
        });

        revealElements.forEach(function (element) {
            observer.observe(element);
        });
    } else {
        revealElements.forEach(function (element) {
            element.classList.add("visible");
        });
    }

    // Close the mobile navigation after the user chooses a section.
    document.querySelectorAll("#mainNavigation .nav-link").forEach(function (link) {
        link.addEventListener("click", function () {
            const menu = document.getElementById("mainNavigation");

            if (menu && menu.classList.contains("show") &&
                window.bootstrap && window.bootstrap.Collapse) {
                window.bootstrap.Collapse.getOrCreateInstance(menu).hide();
            }
        });
    });

    // Smooth in-page navigation, with reduced-motion preferences respected.
    document.querySelectorAll('a[href^="#"]').forEach(function (link) {
        link.addEventListener("click", function (event) {
            const targetId = link.getAttribute("href");

            if (!targetId || targetId === "#") {
                return;
            }

            const target = document.querySelector(targetId);
            if (!target) {
                return;
            }

            event.preventDefault();
            target.scrollIntoView({
                behavior: window.matchMedia("(prefers-reduced-motion: reduce)").matches
                    ? "auto"
                    : "smooth",
                block: "start"
            });
        });
    });
})();
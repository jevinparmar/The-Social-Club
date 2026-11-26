document.addEventListener("DOMContentLoaded", () => {
    // Show / Hide Password toggle
    const toggleButtons = document.querySelectorAll(".toggle-password");
    toggleButtons.forEach((btn) => {
        btn.addEventListener("click", () => {
            const targetId = btn.getAttribute("data-target");
            const input = document.getElementById(targetId);
            if (!input) return;

            const isPassword = input.getAttribute("type") === "password";
            input.setAttribute("type", isPassword ? "text" : "password");
            btn.textContent = isPassword ? "Hide" : "Show";
            btn.setAttribute("aria-label", isPassword ? "Hide password" : "Show password");
        });
    });

    // Client-side confirm password match feedback on registration
    const registerForm = document.getElementById("registerForm");
    if (registerForm) {
        const passwordInput = document.getElementById("id_password");
        const confirmInput = document.getElementById("id_confirm_password");

        const validateMatch = () => {
            if (!confirmInput.value) {
                confirmInput.setCustomValidity("");
                return;
            }
            if (passwordInput.value !== confirmInput.value) {
                confirmInput.setCustomValidity("Passwords do not match.");
            } else {
                confirmInput.setCustomValidity("");
            }
        };

        if (passwordInput && confirmInput) {
            const checkUpper = document.getElementById("check-upper");
            const checkLower = document.getElementById("check-lower");
            const checkNumber = document.getElementById("check-number");
            const checkSpecial = document.getElementById("check-special");

            const updateChecklist = () => {
                const val = passwordInput.value;
                const rules = [
                    [checkUpper, /[A-Z]/.test(val)],
                    [checkLower, /[a-z]/.test(val)],
                    [checkNumber, /\d/.test(val)],
                    [checkSpecial, /[^A-Za-z0-9]/.test(val)],
                ];

                let allValid = true;
                rules.forEach(([el, passed]) => {
                    if (!el) return;
                    const cb = el.querySelector("input[type='checkbox']");
                    if (cb) cb.checked = passed;
                    el.classList.toggle("valid", passed);
                    if (!passed) allValid = false;
                });

                if (val && !allValid) {
                    passwordInput.setCustomValidity("Password must include capital, small, number, and special character.");
                } else {
                    passwordInput.setCustomValidity("");
                }
            };

            passwordInput.addEventListener("input", () => {
                updateChecklist();
                validateMatch();
            });
            confirmInput.addEventListener("input", validateMatch);
        }
    }
});


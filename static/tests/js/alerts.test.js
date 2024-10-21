/** * @jest-environment jsdom */
require('@testing-library/jest-dom');

jest.useFakeTimers()
const alert_message = require("../../js/alerts.js");

describe("Alert Messages Fade", () => {
    test("Should handle when no alerts are present", () => {
        // setting up the fake dom element
        document.body.innerHTML = '';

        // runs the fading function of alert messages
        alert_message();

        // simulating the time advancing
        jest.advanceTimersByTime(3000);

        // checking to see if the alert has faded
        const alert = document.querySelectorAll(".alert");
            expect(alert.length).toBe(0);
    })
})

describe("Alert Messages Fade", () => {
    test("Should make alert message dissappear in 3 seconds", () => {
        // setting up the fake dom element
        document.body.innerHTML = '<div class="alert">Test Alert</div>';

        // runs the fading function of alert messages
        alert_message();

        // simulating the time advancing
        jest.advanceTimersByTime(3000);

        // checking to see if the alert has faded
        const alert = document.querySelectorAll(".alert");
        alert.forEach(alert => {
            expect(alert.className).toContain("fade");
        })

        // simulating the time advancing and element being removed
        jest.advanceTimersByTime(300);
        const alert_removed = document.querySelectorAll(".alert");
        expect(alert_removed.length).toBe(0);
    })
})

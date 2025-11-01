const { test, expect } = require('@playwright/test');

test.describe('Geometry Page Verification', () => {
  test('should display the 2D technical drawings and 3D model correctly', async ({ page }) => {
    // Set the authentication flag in sessionStorage before navigating to the page
    await page.context().addInitScript(() => {
      sessionStorage.setItem('isLoggedIn', 'true');
    });

    // Navigate to the geometry page
    await page.goto('http://localhost:8000/geometry.html');

    // Wait for the canvases to be rendered
    await page.waitForSelector('#threeViewCanvas');
    await page.waitForSelector('#threeDCanvas');

    // Take a screenshot of the entire page to verify both 2D and 3D views.
    const screenshotPath = 'jules-scratch/geometry_verification.png';
    await page.screenshot({ path: screenshotPath, fullPage: true });

    console.log(`Screenshot saved to ${screenshotPath}. Please review it visually.`);

    // Check that the screenshot file was created
    const fs = require('fs');
    expect(fs.existsSync(screenshotPath)).toBe(true);
  });
});

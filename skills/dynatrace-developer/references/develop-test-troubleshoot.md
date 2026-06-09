# Develop — Test & troubleshoot

Scraped from <https://developer.dynatrace.com/develop/>. Each section is one doc page (its path is shown) with the prose and code captured.

## test

`/develop/test-and-troubleshoot/test/`

- Test and troubleshoot

## Testing

- Explanation
- 2-min readThis section provides an overview of the testing frameworks available within Dynatrace Apps, along with best practices and guides on how to implement testing in your app development workflow.

###

#### Create end-to-end tests
Create end-to-end tests for your Dynatrace App.How-to guide

#### Create unit tests
Create comprehensive unit tests with Jest for your Dynatrace Apps.How-to guide

---

## test-and-troubleshoot

`/develop/test-and-troubleshoot/`

- Test and troubleshoot

## Test and Troubleshoot

- 1-min read

###

#### Test
Overview of the testing frameworks available within Dynatrace AppsExplanation

#### Troubleshoot
Index for the troubleshooting guides for Dynatrace AppsExplanation

---

## test/create-end-to-end-tests

`/develop/test-and-troubleshoot/test/create-end-to-end-tests/`

- Test and troubleshoot
- Create E2E tests

## Create end-to-end tests

- How-to guide
- 12-min readEnd-to-end (E2E) testing ensures seamless system functionality and identifies errors before they reach production. This guide explores how to write end-to-end tests using Playwright. We'll cover everything from configuring Playwright to setting up Single Sign-On (SSO) and common pitfalls to avoid. By the end of this guide, you'll have a solid understanding of creating maintainable test suites that will help you catch errors before they become a problem.

### What to consider when writing E2E tests

When writing E2E tests, you need to consider the following:

- Install the app on a target environment. It ensures that you're testing the app in a similar environment to the user (for example, having SSO in place, not running the app on a development server, or similar).

- Avoid hardcoded environment URLs and login information for a smooth login flow to an arbitrary environment. Instead, pass the necessary information as environment variables or read them from configuration files. It allows you to run your tests on different environments, even at various stages (such as development or hardening).

### Install dependencies

To install the required dependencies, run the following command in your terminal:

`tsx
npm init playwright@latest
`

Follow the prompt and select the following options:

- `Where to put your end-to-end tests?`

- write `e2e` and press enter

- `Add a GitHub Actions workflow?`

- select `false` and press enter

- `Install Playwright browsers (can be done manually via 'npx playwright install')?`

- select `true` and press enter

Next, run the following command:

`tsx
npm install --save-dev dotenv
`

The above command will install Playwright and the `dotenv` package. You'll need Playwright to run tests and the `dotenv` package to use `.env` files in your tests.

### Configure Playwright

Ensure that you configure Playwright correctly so it can execute your end-to-end tests. Open the `playwright.config.ts` file in the root folder of your project and change the following content:

`STORAGE_STATE_PATH`: On the top of the file, add a new variable called `STORAGE_STATE_PATH`, which contains a path to a JSON file.

playwright.config.ts
`tsx
// add those linesimport * as path from "path";export const STORAGE_STATE_PATH = path.join(__dirname, 'playwright/.auth/credentials.json');// existing configexport default defineConfig({...
`

`projects`: Playwright projects are logical groups of tests with the same configuration. For example, you can add a project for each browser. For the standard use case, specify a project for `chromium` and `firefox`.

playwright.config.ts
`tsx
/* Configure projects for major browsers */ projects: [ { name: 'setup', testMatch: /auth-setup\.ts/ }, { name: 'chromium', use: { ...devices['Desktop Chrome'], storageState: STORAGE_STATE_PATH, }, dependencies: ['setup'], }, { name: 'firefox', use: { ...devices['Desktop Firefox'], storageState: STORAGE_STATE_PATH, }, dependencies: ['setup'], }, ],
`

`use`: The Playwright use property defines global options for all tests. Here is the basic configuration that you can use.

playwright.config.ts
`tsx
use: { video: { mode: process.env.CI ? 'on': 'on-first-retry', size: { width: 800, height: 450 }, }, trace: { mode: process.env.CI ? 'retain-on-failure': 'on', }, screenshot: { mode: process.env.CI ? 'on': 'only-on-failure', fullPage: false, }, headless: !!process.env.CI, viewport: { width: 1920, height: 1080 }, permissions: ["local-network-access"], },
`

`reporter`: Playwright comes with a few built-in reporters for different needs, such as an HTML reporter

playwright.config.ts
`tsx
reporter: process.env.CI? [ ['line'], ['junit', { outputFile: 'results.xml'}], ['html', { open: 'never'}], ]: [['list'], ['html']],
`

Let's understand the configuration.

- `video`: This property specifies if Playwright records a video while it executes the tests. This video is available in the HTML report. The properties defined will result in the following behavior:

- CI: Playwright always records a video.

- Local: Playwright records a video on the first test retry.

- `trace`: This property specifies if and when Playwright records a trace when it executes the tests. The recorded trace is accessible in the HTML report. The properties defined will result in the following behavior:

- CI: The trace only persists if the test fails. Otherwise, Playwright will discard it.

- Local: The trace is always available.

- `screenshot`: This property specifies if and when Playwright takes a screenshot at the end of the test or after a test fails. The screenshot is accessible in the HTML report. The properties defined will result in the following behavior:

- CI: The screenshot is always available.

- Local: The screenshot is only available when a test fails.

- `headless`: This property specifies if the browser should run in headless or headed mode. The properties defined will result in the following behavior:

- CI: Playwright starts the browser in headless mode.

- Local: Playwright starts the browser in headed mode.

- `reporter`: This property specifies which reporters Playwright should use. The properties defined will result in the following behavior:

- CI: Playwright will use the following reporters on the CI: line, junit, html

- Local: Playwright will use the following reporters locally: list, html

### Set up single sign-on

Before running the end-to-end tests, you need to log in using your Dynatrace user credentials. Add the following content in the `e2e/tests/auth/auth-setup.ts` file.

`e2e/src/utils/setup.ts`: Create a new file called setup.ts within the e2e/src/utils directory. This file will contain the utilities necessary for the login process. Then, paste the following content into it:

e2e/src/utils/setup.ts
`tsx
import { config } from 'dotenv';// reads env vars from .env fileconfig();interface Credentials { user: string; password: string;}// returns user name and password from env varsexport function getLoginCredentials(): Credentials { if (!!process.env.PLATFORM_INTEGRATION_TEST_USER && !!process.env.PLATFORM_INTEGRATION_TEST_PASSWORD) { return { user: process.env.PLATFORM_INTEGRATION_TEST_USER, password: process.env.PLATFORM_INTEGRATION_TEST_PASSWORD, }; } throw Error( `Please create an .env file and set the variable PLATFORM_INTEGRATION_TEST_USER and PLATFORM_INTEGRATION_TEST_PASSWORD`, );}// returns url on which you want to execute the testexport const baseUrl = process.env.ENVIRONMENT_URL;// returns the app idexport const appId = process.env.APP_ID_POSTFIX ? `my.dynatrace.notebooks.${process.env.APP_ID_POSTFIX.toLowerCase()}` : 'local-dev-server';// extends app url with intent or local-dev-server if neededexport const generateSearch = (intent = '') => { const encodedIntent = intent ? `#${encodeURIComponent(intent)}` : ''; const extraSearch = process.env.APP_ID_POSTFIX ? encodedIntent : `?locationAppIds=${encodeURIComponent('http://localhost:3000/ui,local-dev-server')}${encodedIntent}`; return extraSearch;};// returns the app pathexport const appPathInShell = `/ui/apps/${appId}/${generateSearch()}`;export const pageUrl = `${baseUrl}${appPathInShell}`;
`

`e2e/tests/auth/auth-setup.ts`: Create a new file `e2e/tests/auth/auth-setup.ts`, which will contain one test that gets the login credentials from `e2e/src/utils/setup.ts` and log you in. To achieve this, paste the following content into that file:

e2e/tests/auth/auth-setup.ts
`tsx
import { test as setup, expect } from '@playwright/test';import { STORAGE_STATE_PATH } from '../../../playwright.config';import { getLoginCredentials, pageUrl } from '../../src/utils/setup';setup('do login', async ({ page }) => { // go to app url await page.goto(pageUrl); // get user credentials const { user, password } = getLoginCredentials(); /// login await page.getByLabel('Email').fill(user); await page.getByRole('button', { name: 'Next' }).click(); await page.getByRole('textbox', { name: 'Password' }).fill(password); await page.getByRole('button', { name: 'Sign in' }).click(); // wait until platform is loaded await expect(page.getByTestId('app-iframe')).toBeAttached({ timeout: 10_000 }); // Persist the logged in state await page.context().storageState({ path: STORAGE_STATE_PATH });});
`

Let's understand the code.

`e2e/src/utils/setup.ts`:

The `config` import is from the `dotenv` package, which loads environment variables from a `.env` file.

The `Credentials` interface defines the structure of login credentials, with `user` and `password` properties.

The `getLoginCredentials()` function retrieves the login credentials from environment variables (`PLATFORM_INTEGRATION_TEST_USER` and `PLATFORM_INTEGRATION_TEST_PASSWORD`). If you don't set the variables, the function will throw an error, requesting you to set the necessary environment variables.

The code snippet stores the environment variables `ENVIRONMENT_URL` and `APP_ID` in `baseUrl` and `appId`, respectively, and constructs `pageUrl` by combining `environmentUrl` and `appId` using template literals.

`e2e/tests/auth/auth-setup.ts`:

The `test as setup` import from `@playwright/test` means that this test is only used for setup purposes and won't test an actual feature. The `STORAGE_STATE` is a path specified in the `playwright.config.ts` file that defines where Playwright should store the authentication state. The authentication setup uses the `getLoginCredentials, pageUrl` import from `../app/setup` to access the login credentials and URL that points directly to the app.

The `await page.context().storageState({ path: STORAGE_STATE });` defines where Playwright should store the login state. Playwright will use this login state for all other tests to avoid having to authenticate for each test.

### Write your first test

To write a clean first test, you'll need three layers of files, page objects, assertions and the test file itself.

`e2e/src/page-objects/app-landing-page/app-header.po.ts`: First, let's create a page-object containing selectors and methods to interact with your app. In this case, this page object targets the app header. Now, create a new file named `e2e/src/page-objects/app-landing-page/app-header.po.ts` and paste the following content into it.

e2e/src/page-objects/app-landing-page/app-header.po.ts
`tsx
import { FrameLocator, Locator, Page } from '@playwright/test';export class AppHeader { private readonly APP_IFRAME: FrameLocator; public readonly HEADER: Locator; constructor(private page: Page) { this.APP_IFRAME = page.frameLocator('[data-testid="app-iframe"]'); this.HEADER = this.APP_IFRAME.getByRole('navigation'); } async clickAppIcon() { await this.HEADER.click(); }}
`

`e2e/src/page-objects/app-landing-page/app-header.assertion.ts`: This assertion file only contains methods for asserting the page state of your app. In this case, the assertion targets the app header. Next, create a new file named `e2e/src/page-objects/app-landing-page/app-header.assertion.ts` and paste the following content into it.

NoteMoving assertions into a separate file is only helpful in two cases:

- You're using them in several tests or intend to do so.

- They're complex and long. In this case, extract them in an assertion file and give them a descriptive name.

e2e/src/page-objects/app-landing-page/app-header.assertion.ts
`tsx
import { Page, expect } from '@playwright/test';import { AppHeader } from './app-header.po';export class VerifyAppHeader { public readonly AppHeader: AppHeader; constructor(private page: Page) { this.AppHeader = new AppHeader(page); } async verifyAppIsOpen() { await expect(this.AppHeader.HEADER).toBeVisible(); }}
`

`e2e/tests/landing-page/first-test.spec.ts`: Now that you've configured everything, let's write the first test. Create a test file `first-test.spec.ts` in your project's `e2e/tests/landing-page/` directory and add the following content.

e2e/tests/landing-page/first-test.spec.ts
`tsx
import { test } from '@playwright/test';import { VerifyAppHeader } from '../../src/page-objects/app-landing-page/app-header.assertion';import { pageUrl } from '../../src/utils/setup';test.beforeEach(async ({ page }) => { await page.goto(pageUrl);});test('Should open the app successfully', async ({ page }) => { await new VerifyAppHeader(page).verifyAppIsOpen();});
`

Let's understand the files.

`Page objects`: A page object represents your UI in test code. This file includes selectors and methods to interact with your page while testing.

- `Selectors` are usually defined on top of a page object and initialized in the constructor. Playwright recommends using their built-in locators instead of Xpath or CSS selectors. Additionally, selector names should follow the SCREAMING_SNAKE_CASE format.

- `Interaction methods` execute a logically related group of actions on a specific page. The method's name should always target the functionality or the outcome, such as openApp or executeQuery.

`Assertion`: An assertion file should generally relate to a page object. For the page object `app-header.po.ts`, the connected assertion file would be `app-header.assertion.ts`. Additionally, the class name should be the same as the one of the page object but prefixed with `Verify`.

`Test file`: The `test` function defines an individual test case and in this case. We've named the test Should open the app successfully. Within the test, we use Playwright methods on `page` (the Page) to interact with the page and perform assertions. The test does two things:

- `await page.goto(pageUrl)`: The beforeEach method calls this function, which means it runs before every test in that file. The `page.goto` method redirects the test to a new URL, which is in this case the pageUrl coming from the `e2e/src/utils/setup.ts` file.

- `await new VerifyAppHeader(page).verifyAppIsOpen()`: This method calls the `verifyAppIsOpen` method from the'e2e/src/page-objects/app-landing-page/app-header.assertion.ts` file we created earlier which asserts that the header div is visible.

### Run tests

To run your tests, you'll need to do the following:

- Set the environment.

- Add `npm` scripts.

- Ignore Playwright output folders to avoid app reloads.

- Run the tests locally or in your CI.

Here's how:

#### Set environment

Ensure that you configure environment variables before running the tests. The setup supports the `.env` file if you run tests locally. Create a `.env` file in the root directory and add the following content:

.env
`tsx
ENVIRONMENT_URL=APP_ID=PLATFORM_INTEGRATION_TEST_USER=PLATFORM_INTEGRATION_TEST_PASSWORD=
`

NoteReplace the following placeholder:

- with the URL of your Dynatrace environment that hosts your app. Ensure it doesn't end with a `/`, which would cause failures while running the tests.

- with your app's ID.

- with the email address of your test user.

- with the password of your test user.

#### Add `npm` scripts

To run the tests, add the following npm scripts in your `package.json` file:

package.json
`tsx
{ "scripts": { "test:e2e": "playwright test --project=chromium", "test:e2e-ci": "playwright test" }}
`

#### Ignore Playwright output folders to avoid app reloads

Playwright produces output files when it executes tests. The app's hot reloading detects these files by default and triggers page reloads.
Configure the hot reloading mechanism to ignore Playwright output files to avoid such reloads.

app.config.json
`tsx
{ ... "dev": { "fileWatcher": { "ignore": ["test-results/**", "playwright/**", "playwright-report/**"] } }}
`

#### Run tests locally

To run the tests locally, execute the following command in the terminal:

`tsx
npm run test:e2e
`

#### Run tests in CI

To run your tests in CI, follow these steps:

Install the app: Install the new version of your app on the desired environment. The main thing to remember is that you don't override an existing app. You can achieve this by using a unique app ID in `app.config.json`.

Run the tests: Since you have configured headless mode in the config, just run the following command in your CI: `npm run test:e2e-ci`. Ensure that you've configured the required environment variables.

Uninstall the app: You should always uninstall the app, regardless of whether tests fail or pass.

### Debug tests

Writing tests is similar to writing code. You might face a situation where you want to debug your tests. In Playwright, there are some easy ways to debug your tests. Check out the Playwright documentation to learn more about its helpful debugging possibilities.

---

## test/create-unit-tests

`/develop/test-and-troubleshoot/test/create-unit-tests/`

- Test and troubleshoot
- Create unit tests

## Create unit tests

- How-to guide
- 7-min readIn Dynatrace Apps, you can write unit tests using Jest. This guide teaches you how to write unit tests for React components and app functions.

### Test your UI

Testing your app's UI components helps you recognize errors early on. The Strato Design System offers features to help you write unit tests for your React app.

#### Install dependencies

Here are the dependencies you need to install:

- `jest`: Jest is a JavaScript testing framework.

- `ts-node`: Needed to use TypeScript for configuration, such as `jest.config.ts`.

- `ts-jest`: A Jest transformer that allows you to test your TypeScript code. You'll need this as you'll write Dynatrace Apps in Typescript.

- `@types/jest`: Typescript types for Jest.

- `jest-environment-jsdom`: A Jest environment where the UI tests will run.

- `@testing-library/jest-dom`: Provides a set of custom matchers that you can use to extend Jest. Think of a group of methods that already have most of the things you need to test UI components.

- `@testing-library/react`: A required dependency for testing Strato components.

- `@testing-library/user-event`: A required dependency for testing Strato components.

To install the dependencies, run the folowing command:

`tsx
npm i --save-dev jest@^29.0.0 ts-node ts-jest@^29.0.0 @types/jest@^29.0.0 jest-environment-jsdom@^29.0.0 @testing-library/jest-dom @testing-library/react @testing-library/user-event
`

NoteIf you're using React 17 or lower, use the following command to install the required dependencies:
`tsx
npm i --save-dev jest@^29.0.0 ts-node ts-jest@^29.0.0 @types/jest@^29.0.0 jest-environment-jsdom@^29.0.0 @testing-library/jest-dom @testing-library/react@^12.1.5 @testing-library/user-event
`

After installing the dependencies, ensure that the versions for `jest` and `jest-environment-jsdom` are the same.

#### Add types

To get the type information in your Jest tests, you need to add Jest types in the `tsconfig.json` in the `types` array as follows:

tsconfig.json
`tsx
{ "compilerOptions": { ... "types": [ ..., "@types/jest", "@testing-library/jest-dom" ], },}
`

#### Create a configuration file

Dynatrace Apps are written in TypeScript, which Jest can't understand by default. Moreover, Dynatrace Apps are built with the Strato Design System, which requires custom configurations to be testable. To run unit tests using Jest, you need to create a `jest.config.js` file in the root directory of your app with the following code:

jest.config.js
`tsx
const { stratoPreset } = require('@dynatrace/strato-components-testing/jest/preset');/** @type {import('jest').Config} */module.exports = { ...stratoPreset, preset: 'ts-jest', displayName: 'ui', testEnvironment: 'jsdom', roots: ['/ui'], transform: { '^.+\\.(t|j)sx?$': ['ts-jest', { isolatedModules: true }], }, setupFilesAfterEnv: [ // Strato jest mocks '@dynatrace/strato-components-testing/jest/setup', ], moduleNameMapper: { ...stratoPreset.moduleNameMapper, // your other moduleNameMappers },};
`

Here's a description of the settings in the configuration file:

- displayName—the `displayName` that appears in UI when running the test.

- testEnvironment—the environment you use for testing. In this case, you need `jsdom` to have a browser-like environment for testing.

- roots—root of the project from where Jest can start looking for tests.

- setupFiles—modules you want to run before running each test file. They're executed before a test framework like `@testing-library` is loaded. In this case, you're using a setup file from the Strato Design System required to test code written using Strato components.

- transform—specifies how Jest should transform the files before running them. In this case, `.ts`, `.js`, `.tsx`, and `.jsx` are transformed using `ts-jest`.

- setupFilesAfterEnv—add `/jest/setup` so the Jest mocks provided by Strato are used.

- stratoPreset—a set of default configurations required if you're using Strato components. It also uses `moduleNameMappers`, which maps dependencies correctly for Jest.

##### Additional setup files

Depending on the features you use, you may need additional setup files. Below are the SDKs with their setup file imports, which you may need to add to the `setupFiles` array in your `jest.config.js` file:

- `@dynatrace-sdk/navigation/testing`

- `@dynatrace-sdk/user-preferences/testing`

- `@dynatrace-sdk/app-environment/testing`

#### Handling style imports

By default, Jest runs your code as JavaScript. When you import styles into your React component, Jest tries to interpret them as JavaScript and fail. To fix this issue, you can tell Jest to mock the styles in `jest.config.js`, as follows:

jest.config.js
`tsx
{ ... transform: { '.(css|scss|sass|less)$': '/style-mock.ts' },}
`

Add the following content in `style-mock.ts`:

style-mock.ts
`tsx
module.exports = { process() { return { code: 'module.exports = {};' }; },};
`

#### Your first UI unit test

To write your first UI unit test, create a file `First.test.tsx` in the `ui` directory with the following content:

ui/First.test.tsx
`tsx
// importsimport React from 'react';import { render } from '@dynatrace/strato-components-testing/jest';import { screen } from '@testing-library/react';// componentimport { Heading } from '@dynatrace/strato-components/typography';const TestHeading = ({ textValue }) => { return Heading level={1}>{textValue}Heading>;};// testdescribe('Heading component', () => { test('should render the Unit test on screen', () => { render(TestHeading textValue="Unit test" />); expect(screen.getByText('Unit test')).toBeInTheDocument(); });});
`

Let's understand the above test.

First, you have import statements. Besides importing React, you have the `render` and `screen` methods from the Strato Design System, which allow you to render a component, and then, create a test to see what's on the screen. You also have an import from `@testing-library` that extends the `expect` method of `jest`, to allow you to use functions like `toBeInTheDocument`.
Then, you have a component named `Heading` that you're testing in the following test. In real applications, this wouldn't be part of the test code. However, for simplicity in this guide, it's added to the test file.

You have a test suite using the describe and test functions. These functions are part of Jest. In the test, you're using the `Heading` component from the Strato Design System using `Unit test` as the heading value and expecting whether the Unit test value is printed on the screen.

NoteTo use functions like `toBeInTheDocument`, you need to import the `@testing-library/jest-dom` package in all your tests. However, you can import it for all tests by default with the `setupFilesAfterEnv`, as follows:jest.config.js
`tsx
{ ... setupFilesAfterEnv: [`/ui/jest-setup.ts`]}
`
And then import the `@testing-library/jest-dom` in `jest-setup.ts` file as following:jest-setup.ts
`tsx
import '@testing-library/jest-dom';
`
You don't need to import this in any of your tests.

#### Running UI tests

To run the tests, first, you need to create an npm script in `package.json` as follows:

`tsx
{ "scripts": { "test:ui": "jest" }}
`

Now you can run the following command to run the tests:

`tsx
npm run test:ui
`

And you'll be greeted by the following messages:

`tsx
> jest PASS ui ui/First.test.tsx Heading component √ should render the Unit test on screen (23 ms)Test Suites: 1 passed, 1 totalTests: 1 passed, 1 totalSnapshots: 0 totalTime: 4.311 sRan all test suites.
`

TipIf you're using `styled-components`, you might get an error such as `ResizeObserver not found`. To fix it, mock `ResizeObserver` in `jest-setup.ts` as follows:
`tsx
import '@testing-library/jest-dom';global.ResizeObserver = jest.fn().mockImplementation(() => ({ observe: jest.fn(), unobserve: jest.fn(), disconnect: jest.fn(),}));
`

##### Strato Design System `setup` and `clear` functions

The Strato Design System provides two helper functions, `setup` and `clear`, for writing tests. To initialize and clear a set of mocks, call these helper functions in a file which is also set in `setupFilesAfterEnv` within your Jest configuration file, as follows:

jest.config.js
`tsx
/** @type {import('jest').Config} */module.exports = { ..., setupFilesAfterEnv: ['@dynatrace/strato-components-testing/jest/setup'], ...};
`

### Test your app functions

When you run the `generate function` command, the App Toolkit automatically creates a test file. This happens for every function you generate. You also get the `jest.config.js` file created in your app's `api` directory.

Your unit tests have access to all available APIs in the Dynatrace JavaScript Runtime.

#### Mock your fetch functions

If you're using `fetch` to call third party data sources from within your app functions, you need to overwrite its implementation in your unit tests.
The generated test file already contains the following code snippet, which overwrites the global `fetch` function with the mocked `fetchMock` function:

`tsx
const fetchMock = jest.fn();globalThis.fetch = fetchMock;
`

By using the `mockImplementation` or `mockImplementationOnce` function, you can mock the behavior of your actual fetch call.

`tsx
fetchMock.mockImplementationOnce(() => { Promise.resolve({ ok: true, status: 200, json: () => Promise.resolve({ id: 3, firstname: 'John', lastname: 'Doe' }), });});
`

TipIf you have UI and app functions tests, you can use the `projects` property to combine UI and app functions configurations. See the projects property in Jest's documentation.

---

## troubleshoot

`/develop/test-and-troubleshoot/troubleshoot/`

- Test and troubleshoot

## Troubleshoot

- Explanation
- 1-min readThis section provides you with guides on how you can troubleshoot issues when developing custom apps.

###

#### Debug apps
Overview of tools and tips to debug your Dynatrace AppsHow-to guide

#### Develop apps in Safari
Develop your Dynatrace Apps in Safari using local SSL certificates.How-to guide

#### Monitor Dynatrace apps
Set up monitoring for your Dynatrace App.How-to guide

#### Troubleshoot app development
Troubleshooting guide covering common app development issuesReference

#### Troubleshoot app functions
Troubleshoot and solve various issues related to app functionsReference

#### Troubleshoot connectivity
Troubleshoot common App Toolkit connectivity issues.How-to guide

---

## troubleshoot/debug-apps

`/develop/test-and-troubleshoot/troubleshoot/debug-apps/`

- Test and troubleshoot
- Debug apps

## Debug apps

- How-to guide
- 5-min readDynatrace Apps are React apps. You can debug the problems with different tools like:

- Browser developer tools

- Visual Studio Code

### Debugging in Browser

Most browsers offer developer tools that help you to debug your web applications. Although, browsers might have different UIs for developer tools, they provide similar functionalities.

To open the developers tools, use Ctrl + Shift + I (on Windows) or Ctrl + Option + I (on Mac). This is how it looks in Chrome:

#### Debugging UI

The developer tools provide an `Elements` (Chrome) or an `Inspector`(Firefox) tab to debug visual issues. You can do the following with the `Elements` tab:

- View and change the DOM elements

- View and change the CSS

- Inspect the CSS Grid

- Debug CSS Flexbox layouts

To know more about it, take a look at Elements docs.

#### Debugging JavaScript

There are various options to debug your JavaScript application.

- The `console.log`: The ubiquitous `console.log` comes very handy in debugging JavaScript. You can see all the logs in the `Console` tab of the developer tools. It might sound primitive, but it gets work done.

- The `debugger` statement: You can also write a `debugger` statement within your code, just like `console.log`. The debugger statement pauses the execution of the code like a breakpoint. To know more, take a look at debugger statement docs.

- Debugger: Chrome and Firefox provide a debugger under the `Sources` or `Debugger` tab. The debugger allows you to set breakpoints, start and pause the code execution, check the call stack, and a lot more. To know more, read the debugger documentation.

#### Debugging Network requests

Sometimes you might want to see what kind of response you get from a server. The developer tools have a `Network` tab to do it. It allows you to do the following:

- Inspect network activity

- Block requests

- Simulate network connection

- Check the request's timing

- Record network requests

To know more, read the Network documentation.

TipTo learn more about Developer tools, read the Chrome documentation or Firefox documentation.

#### Debugging with React Developer Tools

React Developer Tools is a browser extension that allows you to inspect the React component hierarchies using your browser's developer tools. It's available for Chrome, Firefox, and Microsoft Edge.

After adding the extension, you get two extra tabs in the browser's developer tools: The `Components` and the `Profiler` tabs.

NoteThe AppShell renders apps in an `iframe`. The React developer tools won't work correctly for an iframe. Therefore, you need to detach the apps from the AppShell. Read the AppShell documentation to know more.

##### Debugging the Component tree

The `Components` tab shows you the React component hierarchy. It lets you see and manipulate component state and props. This is how it looks in Chrome:

##### Debugging the performance

The `Profiler` tabs allow you to profile your react application. It's something very similar to the developer tools's `Performance` tab but specific to React. Follow these steps to use the profile:

- Start recording the session by clicking the red circle

- Do the operation in your React application.(For example: click a button, input some text)

- Press the circle again to finish the session. You'd see the component-specific timings as a result.

To know more about React Developer tools, read this tutorial on How To Debug React Components Using React Developer Tools.

### Debugging with VSCode

Projects generated with the App Toolkit include launch configurations for debugging apps with Visual Studio Code. To get started, open the Run and Debug tab on the left bar, then select the configuration you want to use:

Next, select the Run button to start debugging. To see the output of the App Toolkit, select Debug Console in the bottom pane.

#### Debugging the UI

To debug UI code from within Visual Studio Code, use the Launch Chrome for UI debugging configuration. This configuration will start the development server with the App Toolkit and once it's ready, launch Google Chrome. Now you can set breakpoints within the UI source code and reload the page if required.

#### Troubleshooting

If a breakpoint isn't recognized, try removing and adding it again. In cases where breakpoints aren't triggered during app startup, detach the app from the AppShell with the Detach button on the bottom left and reload the page.

### Tips

Following are some tips that might help you while debugging:

- Read the error: Many times developers ignore the error provided by libraries. Take a pause, and read the error. Your solution might be already mentioned.

- Use your editor: Since Dynatrace Apps use TypeScript, your editor might be able to help you in correcting some syntactic issues. Take a look at the TypeScript page to know how it can help you.

- Ask others: Sometimes it's difficult to debug the code you write. Ask your fellow teammate to take a look at your code.

- Share with the community: There is a possibility that your issue is a bug in the underline tooling. In that case, create an issue ticket for the respective team, or send a slack message to the appropriate group.

---

## troubleshoot/develop-apps-in-safari

`/develop/test-and-troubleshoot/troubleshoot/develop-apps-in-safari/`

- Test and troubleshoot
- Develop apps in Safari

## Develop apps in Safari

- How-to guide
- 2-min readTo develop your app in Safari, you need to let the dev server host it via SSL. To do so, complete the following steps.

### Create a certificate

First, you need to create a self-signed root certificate that you'll use to encrypt the connection. Your macOS comes with `openssl`, a terminal command that lets you create certificates as follows:

`tsx
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.crt -sha256 -days 365 -nodes -subj "/CN=localhost"
`

You'll see two files named `key.pem` and `cert.crt` in your current directory.

TipIf you are working on multiple app projects you will use the same certificate and private key for all projects.
Therefore, put the generated files in a central location for easy access.

### Import the certificate

After generating the certificate, you need to import it into Keychain Access as follows:

Open the Keychain Access app on your Mac and select Default Keychains > login from the side menu.

Go to File > Import Items to import your newly generated `cert.crt` file from the earlier step:

Double-click the newly added certificate, which is named localhost, to open a new dialog. Expand the Trust section and, for the When using this certificate option, select Always Trust:

### Configure your application

Now you have to update your app configuration to start using the certificate:

app.config.json
`tsx
{ "environmentUrl": "", "app": { "id": "", "name": "", "version": "0.0.0", "description": "", "scopes": [] }, "server": { "https": { "key": "", "cert": "" } }}
`

Replace the following key-values from your JSON configuration file:

- with the path to the `key` file.

- with the path to the `cert` file.

CautionYou should refrain from committing `key` and `cert` files to your code repository, therefore don't put them in your project directory.

### Run your application

Execute the following command in the project directory to start the dev server:

`tsx
npx dt-app dev
`

This command opens the browser with your app running. You'll see the re-rendering in the browser if you change any code.

---

## troubleshoot/monitor-dynatrace-apps

`/develop/test-and-troubleshoot/troubleshoot/monitor-dynatrace-apps/`

- Test and troubleshoot
- Monitor Dynatrace apps

## Monitor Dynatrace apps

- How-to guide
- 3-min readThis guide will show you how to set up monitoring in your Dynatrace App. Currently, there are two ways in which apps can self-monitor: Real User Monitoring (RUM) collects data about users' interaction with the app, while App Function Logs provide you with information about errors and log data in your app.

#### Prioritizing data privacy

Privacy is of paramount importance in today's digital era. Ensuring privacy isn't only an ethical responsibility but also crucial for maintaining trust with users and staying compliant with ever-evolving data protection regulations. Dynatrace supports you with data privacy and security tools for RUM and App Function Logs. Find details in the respective section.

TipRegularly review and update configurations to align with best practices and data protection standards.

### Real User Monitoring (RUM)

Gain deep insights into your app users' behaviors with Dynatrace's Real User Monitoring. Quickly identify errors, examine response codes, and dive into user session analysis. All monitoring data is channeled either to a custom-configured environment or to the environment where the Dynatrace app is deployed.

NoteSession Replay is currently not supported for custom apps.

#### Setting up RUM

To route your Dynatrace app's monitoring data to a target environment, you need to create a RUM application:

- Go to the desired target environment.

- Open the 'Frontend' app and, from the top-right dropdown menu, choose 'Set up agentless monitoring.'

- Provide a descriptive name and click 'Add web application.'

- From the code section, copy the URL within the `src` attribute (for example `https://js-cdn.dynatrace.com/jstag/1234567890a/bf12345678/1234567890abcdef_complete.js`).

Use this script in your app configuration file for the `selfMonitoringAgent` property:

app.config.json
`tsx
{ "environmentUrl": "", "app": { "id": "", "name": "", "version": "0.0.0", "description": "", "scopes": [], "selfMonitoringAgent": "https://js-cdn.dynatrace.com/jstag/1234567890a/bf12345678/1234567890abcdef_complete.js" }}
`

Save your modifications and redeploy your app. You've now set up RUM monitoring!

TipMake sure you use RUM JavaScript with a version of >1.271 for the Agentless monitoring setup.
To check this (after adding the web application):

- Go to the frontend app and select the newly added web application.

- From the top-right dropdown menu, choose Edit.

- Scroll down and expand the Setup section.

- Select RUM JavaScript updates and check the selected version to be equal/greater than 1.271.

#### Privacy with RUM

Once RUM is initialized, data is channeled to the pre-defined target environment.
Guidance on bolstering security and ensuring data privacy for RUM will lead you through the steps for a secure deployment.

### App function logs

Search within logs for errors or specific custom logs related to your app's functions. Logs for Dynatrace app functions are automatically reported in the environment where the app lives. Consider this when deploying your app to a production environment.

#### Accessing app function logs

No additional configuration is required. Logs are automatically sent to the environment where your Dynatrace app is deployed.

To view them, for instance, launch Notebooks and run the following query:

`tsx
fetch logs| filter dt.app.id == ""
`

#### Privacy with app function logs

When integrating commands like console.log(data) within your Dynatrace application functions, exercise caution regarding the nature and sensitivity of the data you're recording. Logs, irrespective of their level, are amassed in the environment where the application operates. Our comprehensive guide on log masking provides techniques to circumvent unintended data exposures.

### App function traces

Investigate response times, external request response times, and codes from your app functions. The traces are automatically reported to the environment where the app is executed.

You can easily investigate your app function's traces in the Distributed Tracing app. To find the correct traces, use the AppId with the `Service` filter tag and the specific app function name with the `Endpoint` filter tag.

### Configure log level and traces reporting

- Go to General

- Expand the App Monitoring Settings panel and:

- Configure the global log level for all Dynatrace function logs.

- Toggle the reporting of traces on and off.

For app-specific configurations, you can define separate settings at the app level.

---

## troubleshoot/troubleshoot-app-development

`/develop/test-and-troubleshoot/troubleshoot/troubleshoot-app-development/`

- Test and troubleshoot
- Troubleshoot app development

## Troubleshoot app development

- 1-min readDynatrace has a list of supported browsers which works well with it. Take a look at Dynatrace web UI requirements.

If you come across issues on these supported browsers when working on apps, you can take a look at the following:

- Browser plugins

- Browser security settings

### Browser plugins

Browser plugins interfere with app functionality. Disable all plugins if you face an issue.

### Browser security settings

Some of the browser security settings also interfere with app development. The following section describes the common issues with the solution for each browser.

#### Microsoft Edge

##### Third-part cookies

Blocking third-party cookies breaks the SDK injection. It leads to an endless loop of `Uncaught (in promise) Error: No environmentUrl value provided` console errors and making the browser unresponsive.

Solution: Open the `edge://settings/content/cookies` page via address bar and disable the `Block third-party cookies` setting.

#### Google Chrome

##### Third-part cookies

Blocking third-party cookies leads to `DOMException: Failed to read the 'sessionStorage' property from 'Window': Access is denied for this document` console error.

Solution: Open the `chrome://settings/cookies` page via address bar and disable the `Block third-party cookies` setting.

##### Connect to local network

Selecting Block on the popup asking to allow `Look for and connect to any device on your local network` leads to a `404 This application doesn't exist` error.

Solution: When you see this popup for the first time, select Allow.

If you've accidentally clicked on Block before:

- Enter `chrome://settings/content/all?searchSubpage=apps.dynatrace.com` in the address bar to access your Chrome settings page.

- Expand the entry for the URL of your tenant.

- Change the setting for Local network access to either Allow or Ask.

#### Mozilla Firefox

##### Enhanced tracking protection

Enabling `Enhanced tracking protection` crashes the browser with `ResizeObserver loop completed with undelivered notifications` console error when Firefox developer tools are open.

Solution: Turn off the Enhanced tracking protection for the site. Look at this article to learn how to disable it per site.

---

## troubleshoot/troubleshoot-app-functions

`/develop/test-and-troubleshoot/troubleshoot/troubleshoot-app-functions/`

- Test and troubleshoot
- Troubleshoot app functions

## Troubleshoot app functions

- 3-min readCode written in app functions, Dynatrace Workflows, or Dynatrace Notebooks is executed within the Dynatrace JavaScript runtime. This page provides an overview of the issues
that you might encounter while developing functions and suggested solutions.

### Serialization errors

JSON serialization errors ("Failed to serialize result to JSON") might occur when returning a value from a function.

Whenever an app function returns a value, the runtime internally calls
`JSON.stringify`
to convert the given value to a JSON representation. Therefore, the same
limitations
also apply when returning a value from a function:

- The returned value must not contain a circular reference.

- The returned value must not be or contain a
`BigInt`.
Refer to the
MDN documentation on how to use `BigInt` within JSON
for a workaround.

### Event loop behavior

The behavior of deployed Dynatrace app functions differs from that of other JavaScript runtimes like Bun or Deno. Deployed Dynatrace app functions always wait for the JavaScript event loop to finish. For example, you might expect your function invocation to finish immediately rather than waiting for five seconds. This isn't the case, though. The function runs until the timeout finishes.

`tsx
export default function () { setTimeout(() => { console.log('Timer completed.'); }, 5000);}
Promises` that never resolve or reject can behave in a similar way. You might encounter issues with third-party packages that do work in the background if those background tasks aren't gracefully shut down.
In such cases, your Dynatrace app function will appear stuck and eventually run into a timeout error if the event loop doesn't terminate.

### DNS errors

Due to platform limitations, you might encounter DNS error messages such as:

`tsx
dns error: Device or resource busy (os error 16)
`

There are two primary causes of this error:

- The host targeted by an HTTP request doesn't exist, for example, due to a typo.

- The system is overloaded because too many requests are sent concurrently. This error is standard when ingesting a lot of data split into several requests, especially when you don't `await` such requests. Consider sending all your data in a single request (if supported by the server) or batch your requests instead.

#### Batching requests

Find a simple implementation for request batching below. Note that this code only serves as a minimal example. Consider handling errors and potential rate limits of the remote service gracefully in a production environment.

`tsx
async function fetchInBatches(urls: string[], batchSize: number): Promiseunknown[]> { const results: unknown[] = []; for (let i = 0; i urls.length; i += batchSize) { const batch = urls.slice(i, i + batchSize); const batchResults = await Promise.all( batch.map((url) => fetch(url).then((res) => res.json() as Promiseunknown>)), ); results.push(...batchResults); } return results;}export default async function () { const urls = [ 'https://some-api.example.com/item/1', 'https://some-api.example.com/item/2', 'https://some-api.example.com/item/3', 'https://some-api.example.com/item/4', 'https://some-api.example.com/item/5', 'https://some-api.example.com/item/6', // ... ]; const batchSize = 5; // Adjust this number based on expected load const allData = await fetchInBatches(urls, batchSize); console.log(allData);}
`

---

## troubleshoot/troubleshoot-connectivity

`/develop/test-and-troubleshoot/troubleshoot/troubleshoot-connectivity/`

- Test and troubleshoot
- Troubleshoot connectivity

## Troubleshoot connectivity

- How-to guide
- 8-min readConnectivity issues may arise if you're trying to use the App Toolkit from a company network. These can include network issues, proxy issues, firewall issues, single sign-on issues, etc. The following guide will help you solve those issues.

### Install the latest version

First, ensure you're using the latest version of App Toolkit before troubleshooting. The latest version is available at the public npm registry.

You should also ensure you're using a Node.js version officially supported by the App Toolkit (usually the latest LTS version of Node.js). App Toolkit will warn you if you use a Node.js version that's not officially supported with the following message:

`tsx
dt-app is operating in an unofficially supported Node.js environment.To prevent potential issues, it's recommended to utilize the app with Node.js ${majorNode.jsVersion}.
`

If you see this message, adjust the version of your Node.js environment accordingly.

### Verify access to the npm registry

You should also confirm that npm has access to the registry by running the following command in the terminal:

`tsx
npm ping
`

Following is the expected output:

`tsx
npm notice PING https://registry.npmjs.org/npm notice PONG 335ms
`

This output means that npm has access to the public registry. If npm doesn't have access to the official registry, this hints towards a networking issue likely caused by a proxy or firewall in your network. Configure your network and your machine in a way that allows npm and, subsequently, the App Toolkit to access the public npm repository.

### Troubleshooting

This guide helps identify connectivity issues when accessing Dynatrace resources on your corporate network. Follow the commands and compare your machine's outputs with the expected ones. If there are any deviations, go to the connectivity issues section to troubleshoot.

You need to replace the `Environment-Id` with your actual environment ID in the following examples.

#### Connectivity of your machine

You'll see if you can access Dynatrace Single Sign-On (SSO) and your environment.

##### Access Single Sign-On server

To start, check if your machine can access the Dynatrace environment using curl or a similar tool. It tests whether you can reach the Dynatrace Single Sign-On server and whether your machine can access hosts outside your corporate network.

`tsx
curl -I https://sso.dynatrace.com
`

The following output containing a 200 OK is expected:

`tsx
HTTP/2 200...
`

Show full example response output
`tsx
HTTP/2 200date: Thu, 01 Feb 2024 10:10:10 GMTcontent-type: text/htmlcontent-length: 2281set-cookie: ; Expires=Thu, 10 Feb 2024 10:10:10 GMT; Path=/set-cookie: ; Expires=Thu, 10 Feb 2024 10:10:10 GMT; Path=/; SameSite=None; Securex-frame-options: denyframe-options: denyx-xss-protection: 1; mode=blockx-content-type-options: nosniffcontent-security-policy: default-src 'self' https://static.sso.dynatrace.com https://dt-cdn.net; script-src 'self' https://www.google.com/recaptcha/ https://www.gstatic.com/recaptcha/ https://static.sso.dynatrace.com ; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://dt-cdn.net https://static.sso.dynatrace.com; frame-ancestors 'none'; frame-src 'self' https://www.google.com/recaptcha/x-content-security-policy: default-src 'self' https://static.sso.dynatrace.com https://dt-cdn.net; script-src 'self' https://www.google.com/recaptcha/ https://www.gstatic.com/recaptcha/ https://static.sso.dynatrace.com ; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://dt-cdn.net https://static.sso.dynatrace.com; frame-ancestors 'none'; frame-src 'self' https://www.google.com/recaptcha/strict-transport-security: max-age=31536000; preloadcache-control: private, no-store, must-revalidatepragma: no-cacheset-cookie: b925d32c=; Path=/; Domain=sso.dynatrace.com; Expires=Thu, 01-Jan-1970 00:00:00 GMT; Max-Age=0; Secure; HttpOnly; SameSite=Noneset-cookie: ssoCSRFCookie=; Path=/; Domain=.dynatrace.com; Expires=Thu, 01-Jan-1970 00:00:00 GMT; Max-Age=0; Secure; SameSite=None
`

The Dynatrace SSO server is reachable and responding to your requests. It also means your machine can reach hosts outside your corporate network.

##### Access your environment

The following command checks if you can access your Dynatrace environment to access your data. This tests if your specific environment is reachable.

`tsx
curl -I https://Environment-Id>.apps.dynatrace.com/
`

The following output containing a 401 Unauthorized status is expected, as you aren't yet authenticated.

`tsx
HTTP/2 401...
`

It means your environment is reachable from your machine within the corporate network, and your Dynatrace environment is available.

The last command is to check access to your Dynatrace environment with SSO authentication and whether you can facilitate the authentication process. The authentication process is complex, sending and receiving many requests and responses.

`tsx
curl -I https://Environment-Id>.apps.dynatrace.com/platform/oauth2/authorization/dynatrace-sso
`

The following output containing a 302 Found status is expected:

`tsx
HTTP/2 302...
`

It means that Dynatrace SSO is reachable for the authentication for your Dynatrace environment. You get a 302 in this case because curl doesn't follow redirects.

If you don't receive these outputs, refer to this guide's connectivity issues section.
If you have gotten those outputs, try the same Node.js procedure to ensure the Node.js application has identical connectivity. Sometimes, Node.js is blocked from accessing the outside network within corporate networks. Follow along in the next section of this guide.

#### Connectivity of Node.js

As Node.js is your app's main development environment, access to all relevant resources is necessary. Check the following commands to ensure that Node.js is working correctly.

##### Access Single Sign-On server

Execute the first command to access Dynatrace SSO:

`tsx
node -e "fetch('https://sso.dynatrace.com').then(console.log)"
`

The following output containing a 200 OK is expected:

`tsx
... status: 200, ... statusText: 'OK', ...
`

Show full example response output
`tsx
Response { [Symbol(realm)]: null, [Symbol(state)]: { aborted: false, rangeRequested: false, timingAllowPassed: true, requestIncludesCredentials: true, type: 'default', status: 200, timingInfo: { startTime: 39.133354, redirectStartTime: 0, redirectEndTime: 0, postRedirectStartTime: 39.133354, finalServiceWorkerStartTime: 0, finalNetworkResponseStartTime: 0, finalNetworkRequestStartTime: 0, endTime: 0, encodedBodySize: 1270, decodedBodySize: 0, finalConnectionTimingInfo: null }, cacheState: '', statusText: 'OK', headersList: HeadersList { cookies: [Array], [Symbol(headers map)]: [Map], [Symbol(headers map sorted)]: null }, urlList: [ URL {} ], body: { stream: undefined } }, [Symbol(headers)]: HeadersList { cookies: [], [Symbol(headers map)]: Map(18) { 'date' => [Object], 'content-type' => [Object], 'content-length' => [Object], 'connection' => [Object], 'set-cookie' => [Object], 'server-timing' => [Object], 'x-oneagent-js-injection' => [Object], 'x-frame-options' => [Object], 'frame-options' => [Object], 'x-xss-protection' => [Object], 'x-content-type-options' => [Object], 'content-security-policy' => [Object], 'x-content-security-policy' => [Object], 'strict-transport-security' => [Object], 'cache-control' => [Object], 'pragma' => [Object], 'vary' => [Object], 'content-encoding' => [Object] }, [Symbol(headers map sorted)]: null }}
`

##### Access your environment

Execute the following command to see if you can access your Dynatrace environment:

`tsx
node -e "fetch('https://.apps.dynatrace.com').then(console.log)"
`

The following output containing a 401 Unauthorized status is expected, as you aren't yet authenticated.

`tsx
... status: 401, ... statusText: 'Unauthorized', ...
`

Execute the following command to see if you can access the authorization APIs of your environment:

`tsx
node -e "fetch('https://.apps.dynatrace.com/platform/oauth2/authorization/dynatrace-sso').then(console.log)"
`

The following output containing a 200 OK status is expected:

`tsx
... status: 200, ... statusText: 'OK', ...
`

If you don't receive these outputs, refer to this guide's connectivity issues section.

If you did receive these outputs, everything should work as expected if you develop your app with the help of App Toolkit.

### Connectivity issues

If you don't receive the desired outputs of the above commands, several problems might occur. The most common error messages are outlined in the following table and usually indicate a proxy or firewall issue.

 |
 | CURL Error | Node.js Error | Interpretation
 | CURLE_COULDNT_RESOLVE_HOST | ENOTFOUND | The host couldn't be found, something is blocking DNS resolution.
 | CURLE_OPERATION_TIMEDOUT | ETIMEDOUT | The host couldn't be reached, the request timed out.
 | CURLE_REMOTE_ACCESS_DENIED | ECONNREFUSED | The connection was refused by some entity, either the host or some other server.
 | CURLE_RECV_ERROR | ECONNRESET | The connection has been reset by some entity, either the client or some other server.
If you need further information or experience issues not listed here, refer to the curl documentation for detailed information curl. This can help identify your error more quickly. If you find different HTTP error codes, refer to HTTP response status codes for more details.
The most likely culprits in this respect are misconfigured proxy servers and enterprise firewall software.

#### Proxy server

If you don't configure a proxy server correctly, you can experience connection issues.

If your company requires a proxy server for outbound connections, you must configure the App Toolkit with the `DT_APP_HTTPS_PROXY` environment variable to use the proxy server.

Use the following format to configure your proxy server:

`tsx
DT_APP_HTTPS_PROXY=http{s}://{:@}:
`

The curly braces (`{}`) identify optional components.

TipIf you still see connection issues after using this setup, it could be due to an enterprise firewall blocking outbound connections.

#### Firewall

If the proxy isn't the culprit, an enterprise firewall might be actively tampering with connections. App Toolkit is a relatively unknown application. It might be blocked by default in enterprise firewall products, hindering access to the Dynatrace environment. Make sure to unblock the App Toolkit in the corporate firewall or create specific firewall rules to allow as unrestricted access as possible for the App Toolkit.

A common issue you might find is the `SELF_SIGNED_CERT_IN_CHAIN` error. You can work around this by adding your PEM certificate to the NPM config with the following command:

`tsx
npm config set cafile /path/to/cert.pem
`

Contact your in-house IT department for further assistance if you run into any proxy server or firewall issues.

#### GitHub access

If none of the previous solutions work, there's a workaround that might help. When you create a new app with the App Toolkit, it fetches the templates for scaffolding your app from GitHub. Sometimes this process might fail due to your system's restrictions. You can work around this by downloading the templates manually, and using the `--template-dir` option from the App Toolkit.

`tsx
npx dt-app@latest create --template-dir ./path-to-templates-repo/templates/default
`

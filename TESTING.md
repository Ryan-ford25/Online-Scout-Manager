# Testing

![Online Scout Manager on different screen sizes](assets/documentation/am-i-responsive.png)

Visit the deployed site here: [Online Scout Manager](https://online-scout-badge-manager-63d33c684e7e.herokuapp.com/)

> [!NOTE]  
> Return back to the [README.md](README.md) file.

This document outlines the testing processes and results for the **Online Scout Manager** web application. It ensures that all features function as expected, meet accessibility standards, and provide an optimal user experience.

---

<a id=contents></a>

## CONTENTS

- [AUTOMATED TESTING](#automated-testing)
  - [Code Validation](#code-validation)
  - [HTML Validation Results](#html)
  - [CSS Validation Results](#css)
  - [JavaScript Validation Results](#javascript)
  - [Python Validation Results](#python)
  - [Lighthouse](#lighthouse)
- [MANUAL TESTING](#manual-testing)
  - [Full Testing](#full-testing)
  - [Browser Compatibility](#browser-compatibility)
  - [Responsiveness](#responsiveness)
  - [Defensive Programming](#defensive-programming)
  - [User Story Testing](#user-story-testing)
  - [Bugs](#bugs)

<br>
<hr>

Testing was an **integral part of the development process**, ensuring the website remained both **functional and user-friendly** at every stage. By conducting **continuous testing**, potential issues were identified early, allowing for swift resolution and a more efficient workflow.

**Chrome Developer Tools** played a crucial role throughout development, providing real-time insights into performance, responsiveness, and debugging. This proactive approach helped streamline development and ensure the final product adhered to high-quality standards.

Additionally, **ChatGPT** served as a key resource for refining ideas, optimizing content, and overcoming technical challenges. By offering structured guidance, best practices, and alternative solutions, it contributed to improving both the efficiency of development and the overall quality of the final product.

To guarantee **cross-device compatibility**, every screen was rigorously tested across various **screen sizes and devices** using Chrome Developer Tools. This process ensured that Echoes of Light was fully responsive, providing a seamless user experience across **desktops, tablets, and mobile devices**.

---

<a id=automated-testing></a>

## AUTOMATED TESTING

A series of **automated testing** tools were used on the site to check the code for web standard compliance and errors. These tools ensured repeatable, scalable, and performance-driven results throughout the site’s development.

---

<a id=code-validation></a>

## Code Validation

<a id=html></a>

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | Screenshot | Notes |
| --- | --- | --- |
| Home | <img src="assets/documentation/home-page-html-validator.png" width=700 alt="Home page Screenshot"> | Pass: No Errors. |
| Leader Dashboard | <img src="assets/documentation/leader-dashboard-html-validation.png" width=700 alt="Leader Dashboard Screenshot"> | Pass: No Errors <br> Information: The Validator flagged a 'trailing slash' however it doesn't affect the site, but to fix this I found the syntax error in the 'login.html' file and deleted it. |
| Scout Dashboard | <img src="assets/documentation/scout-dashboard-html-validation.png" width=700 alt="Scout Dashboard Screenshot"> | Pass: No Errors |
| Sign In | <img src="assets/documentation/signin-html-validation.png" width=700 alt="Sign In Screenshot"> | Pass: No Errors |
| Sign Up | <img src="assets/documentation/signup-html-validation.png" width=700 alt="Sign Up Screenshot">  | Pass: No Errors |
| Sign Out |  <img src="assets/documentation/signout-html-validation.png" width=700 alt="Sign Out Screenshot">  | Pass: No Errors |
| Badges |  <img src="assets/documentation/badges-html-validation.png" width=700 alt="Badges Screenshot">  | Pass: No Errors |
| Add Badge |  <img src="assets/documentation/add-badge-html-validation.png" width=700 alt="Add Badge Screenshot">  | Pass: No Errors |
| Edit Badge |  <img src="assets/documentation/edit-badge-html-validation.png" width=700 alt="Edit Badge Screenshot">  | Pass: No Errors |
| Bade Detail |  <img src="assets/documentation/badge-detail-html-validation.png" width=700 alt="Badge Detail Screenshot"> | Pass: No Errors |
| Blog Page |  <img src="assets/documentation/blog-html-validation.png" width=700 alt="Blog Page Screenshot">  | Pass: No Errors |
| Blog Post |  <img src="assets/documentation/blog-post-html-validation.png" width=700 alt="Blog Post Screenshot">  | Pass: No Errors |
| Create Post |  <img src="assets/documentation/create-post-html-validation.png" width=700 alt="Create Post Screenshot">  | Pass: No Errors |
| Manage Scouts |  <img src="assets/documentation/manage-scouts-html-validation.png" width=700 alt="Manage Scouts Screenshot">  | Pass: No Errors |

<a id=css></a>

---

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files. Which passed with no errors.

<img src="assets/documentation/css-validator.png" alt="CSS validator screenshot" width=750>

---
<a id=javascript></a>

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| comments.js | <img src="assets/documentation/comment-jshint-validator.png" alt="comments.js JShint validator screenshot" width=750> | Pass: No Errors <br> 1 'Undefined' message as bootstrap link is in the base.html file. |
| delete-badge.js | <img src="assets/documentation/deletebadge-jshint-validator.png" alt="delete-badge.js JShint validator screenshot" width=750>| One Warning: The Jshint tool displayed the warning "Functions declared within loops referencing an outer scoped variable may lead to confusing semantics. (button) <br> After doing some research I found that this wasn't a pressing issue as the code has been functioning as it should through all other tests, but it could be solved by extracting the function out of the loop.|
| requirements.js | <img src="assets/documentation/addrequirement-jshint.validator.png" alt="requirements.js JShint validator screenshot" width=750> |  Pass: No Errors. |

---

<a id=python></a>

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

#### Validation For Online Scout Manager Project
| File | Screenshot | Notes |
| --- | --- | --- |
| asgi.py | <img src="assets/documentation/osm-asgi-py.png" width=700 alt="asgi.py validator screenshot">  | Pass: No Errors |
| settings.py | <img src="assets/documentation/osm-setting-py.png" width=700 alt="settings.py validator screenshot"> | Pass: No Errors |
| urls.py | <img src="assets/documentation/osm-urls-py.png" width=700 alt="asgi.py urls.py screenshot"> | Pass: No Errors |
| wsgi.py | <img src="assets/documentation/osm-wsgi-py.png" width=700 alt="wsgi.py validator screenshot"> | Pass: No Errors |

#### Validation For Accounts App
| File | Screenshot | Notes |
| --- | --- | --- |
| adapters.py | <img src="assets/documentation/accounts-adapters-py.png" width=700 alt="accounts adapter.py validator screenshot"> | Pass: No Errors |
| admin.py | <img src="assets/documentation/accounts-admin-py.png" width=700 alt="accounts admin.py validator screenshot"> | Pass: No Errors |
| apps.py | <img src="assets/documentation/accounts-apps-py.png" width=700 alt="accounts apps.py validator screenshot">| Pass: No Errors |
| forms.py | <img src="assets/documentation/accounts-forms-py.png" width=700 alt="accounts forms.py validator screenshot"> | Pass: No Errors |
| models.py | <img src="assets/documentation/accounts-models-py.png" width=700 alt="accounts models.py validator screenshot"> | Pass: No Errors |
| urls.py | <img src="assets/documentation/accounts-urls-py.png" width=700 alt="accounts urls.py validator screenshot"> | Pass: No Errors |
| utils.py | <img src="assets/documentation/accounts-utils-py.png" width=700 alt="accounts utils.py validator screenshot"> | Pass: No Errors |
| views.py | <img src="assets/documentation/accounts-views-py.png" width=700 alt="accounts views.py validator screenshot"> | Pass: No Errors |

#### Validation For Add Badge App
| File | Screenshot | Notes |
| --- | --- | --- |
| admin.py | <img src="assets/documentation/add-badge-admin-py.png" width=700 alt="add badge admin.py validator screenshot"> | Pass: No Errors |
| apps.py | <img src="assets/documentation/add-badge-apps-py.png" width=700 alt="add badge apps.py validator screenshot">| Pass: No Errors |
| forms.py | <img src="assets/documentation/add-badge-forms-py.png" width=700 alt="add badge forms.py validator screenshot"> | Pass: No Errors |
| models.py | <img src="assets/documentation/add-badge-models-py.png" width=700 alt="add badge models.py validator screenshot"> | Pass: No Errors |
| urls.py | <img src="assets/documentation/add-badge-urls-py.png" width=700 alt="add badge urls.py validator screenshot"> | Pass: No Errors |
| views.py | <img src="assets/documentation/add-badge-views-py.png" width=700 alt="add badge views.py validator screenshot"> | Pass: No Errors |

#### Validation For Blog App
| File | Screenshot | Notes |
| --- | --- | --- |
| admin.py | <img src="assets/documentation/blog-admin-py.png" width=700 alt="blog admin.py validator screenshot"> | Pass: No Errors |
| apps.py | <img src="assets/documentation/blog-apps-py.png" width=700 alt="blog apps.py validator screenshot">| Pass: No Errors |
| forms.py | <img src="assets/documentation/blog-forms-py.png" width=700 alt="blog forms.py validator screenshot"> | Pass: No Errors |
| models.py | <img src="assets/documentation/blog-models-py.png" width=700 alt="blog models.py validator screenshot"> | Pass: No Errors |
| urls.py | <img src="assets/documentation/blog-urls-py.png" width=700 alt="blog urls.py validator screenshot"> | Pass: No Errors |
| views.py | <img src="assets/documentation/blog-views-py.png" width=700 alt="blog views.py validator screenshot"> | Pass: No Errors |

#### Validation For Dashboard App
| File | Screenshot | Notes |
| --- | --- | --- |
| apps.py | <img src="assets/documentation/dashboard-apps-py.png" width=700 alt="dashboard apps.py validator screenshot">| Pass: No Errors |
| urls.py | <img src="assets/documentation/dashboard-urls-py.png" width=700 alt="dashboard urls.py validator screenshot"> | Pass: No Errors |
| views.py | <img src="assets/documentation/dashboard-views-py.png" width=700 alt="dashboard views.py validator screenshot"> | Pass: No Errors |

---

<a id=lighthouse></a>

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues, the tool tests the websites Performance, Accessibility, Best Practices and SEO(Search Engine Optimization). Thankfully no major issues were found and all pages achieved great scores across both mobile and desktop.

### Online Scout Manager App - Mobile Testing
| Page | Size | Screenshot |
| --- | --- | --- |
| Home | Mobile | <img src="assets/documentation/home-page-lighthouse-mobile.png" width=500 alt="Home Page Mobile Lighthouse Score"> | 
| Sign In | Mobile | <img src="assets/documentation/signin-lighthouse-mobile.png" width=500 alt="Sign In Mobile Lighthouse Score"> |
| Sign Up | Mobile | <img src="assets/documentation/signup-lighthouse-mobile.png" width=500 alt="Sign Up Mobile Lighthouse Score"> |
| Sign Out | Mobile | <img src="assets/documentation/signout-lighthouse-mobile.png" width=500 alt="Sign Out Mobile Lighthouse Score"> |
| Leader Dashboard | Mobile | <img src="assets/documentation/leader-dashboard-lighthouse-mobile.png" width=500 alt="Leader Dashboard Mobile Lighthouse Score"> | 
| Scout Dashboard | Mobile | <img src="assets/documentation/scout-dashboard-lighthouse-mobile.png" width=500 alt="Scout Dashboard Mobile Lighthouse Score"> | 
| Badges | Mobile | <img src="assets/documentation/badges-lighthouse-mobile.png" width=500 alt="Badges Mobile Lighthouse Score"> |
| Badge Detail | Mobile | <img src="assets/documentation/badge-detail-lighthouse-mobile.png" width=500 alt="Badge Detail Mobile Lighthouse Score"> | 
| Add Badge | Mobile | <img src="assets/documentation/add-badge-lighthouse-mobile.png" width=500 alt="Add Badge Mobile Lighthouse Score"> | 
| Edit Badge | Mobile | <img src="assets/documentation/edit-badge-lighthouse-mobile.png" width=500 alt="Edit Badge Mobile Lighthouse Score"> | 
| Blog | Mobile | <img src="assets/documentation/blog-lighthouse-mobile.png" width=500 alt="Blog Mobile Lighthouse Score"> | 
| Blog Post | Mobile | <img src="assets/documentation/blog-post-lighthouse-mobile.png" width=500 alt="Blog Post Mobile Lighthouse Score"> | 
| Create Post | Mobile | <img src="assets/documentation/create-post-lighthouse-mobile.png" width=500 alt="Create Post Mobile Lighthouse Score"> | 
| Manage Scouts | Mobile | <img src="assets/documentation/manage-scouts-lighthouse-mobile.png" width=500 alt="Manage Scouts Mobile Lighthouse Score"> | 

### Online Scout Manager App - Desktop Testing
| Page | Size | Screenshot | 
| --- | --- | --- | 
| Home | Desktop | <img src="assets/documentation/home-page-lighthouse-desktop.png" width=500 alt="Home Page Desktop Lighthouse Score"> | 
| Sign In | Desktop | <img src="assets/documentation/signin-lighthouse-desktop.png" width=500 alt="Sign In Desktop Lighthouse Score"> |
| Sign Up | Desktop | <img src="assets/documentation/signup-lighthouse-desktop.png" width=500 alt="Sign Up Desktop Lighthouse Score"> |
| Sign Out | Desktop | <img src="assets/documentation/signout-lighthouse-desktop.png" width=500 alt="Sign Out Desktop Lighthouse Score"> |
| Leader Dashboard | Desktop | <img src="assets/documentation/leader-dashboard-lighthouse-desktop.png" width=500 alt="Leader Dashboard Desktop Lighthouse Score"> | 
| Scout Dashboard | Desktop | <img src="assets/documentation/scout-dashboard-lighthouse-desktop.png" width=500 alt="Scout Dashboard Desktop Lighthouse Score"> | 
| Badges | Desktop | <img src="assets/documentation/badges-lighthouse-desktop.png" width=500 alt="Badges Desktop Lighthouse Score"> |
| Badge Detail | Desktop | <img src="assets/documentation/badge-detail-lighthouse-desktop.png" width=500 alt="Badge Detail Desktop Lighthouse Score"> | 
| Add Badge | Desktop | <img src="assets/documentation/add-badge-lighthouse-desktop.png" width=500 alt="Add Badge Desktop Lighthouse Score"> | 
| Edit Badge | Desktop | <img src="assets/documentation/edit-badge-lighthouse-desktop.png" width=500 alt="Edit Badge Desktop Lighthouse Score"> | 
| Blog | Desktop | <img src="assets/documentation/blog-lighthouse-desktop.png" width=500 alt="Blog Desktop Lighthouse Score"> | 
| Blog Post | Desktop | <img src="assets/documentation/blog-post-lighthouse-desktop.png" width=500 alt="Blog Post Desktop Lighthouse Score"> | 
| Create Post | Desktop | <img src="assets/documentation/create-post-lighthouse-desktop.png" width=500 alt="Create Post Desktop Lighthouse Score"> | 
| Manage Scouts | Desktop | <img src="assets/documentation/manage-scouts-lighthouse-desktop.png" width=500 alt="Manage Scouts Desktop Lighthouse Score"> | 

---

<a id=manual-testing></a>

## Manual Testing

<a id=full-testing></a>

### Full Testing

This section outlines the **manual testing** process conducted to ensure the website functions correctly across different devices, screen sizes, and user interactions. Each test was performed methodically to identify potential issues with responsiveness, usability, and accessibility, with results documented for further improvements. Additional testing was carried out by friends and family on a variety of devices and screen sizes.

---

<a id=browser-compatibility></a>

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | <img src="assets/documentation/chrome-screenshot.png" width=700> | Works as expected |
| Firefox | <img src="assets/documentation/firefox-screenshot.png" width=700>  | Works as expected |
| Edge | <img src="assets/documentation/microsoft-edge-screenshot.png" width=700>  | Works as expected |
| Opera | <img src="assets/documentation/opera-screenshot.png" width=700>  | Works as expected |

---

<a id=responsiveness></a>

## Responsiveness

In addition to testing my deployed site on different devices, I thoroughly tested its responsiveness using Chrome Developer Tools.
I researched the narrowest width of modern devices on Stack Exchange and based my testing on 320px as a standard minimum width.
Additionally, I used the Mobile First Plugin, a Chrome extension designed to test site responsiveness across different devices.

---

### Home Screen

#### Mobiles
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPhone 5 <br> <img src="assets/documentation/iphone5-home.png" height=400> | 320 | 568 |
| iPhone 13 <br> <img src="assets/documentation/iphone13-home.png" height=400> | 390 | 844 |
| Samsung S20 <br> <img src="assets/documentation/samsung-s20-home.png" height=400> | 360 | 800 |
| OnePlus Nord 2 <br> <img src="assets/documentation/oneplus-home.png" height=400> | 412 | 915 |

#### Tablets
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPad Mini <br> <img src="assets/documentation/ipadmini-home.png" height=400> | 768 | 1024 |
| Galaxy Tab S7 <br> <img src="assets/documentation/galaxytab-home.png" height=400> | 800 | 1280 |
| iPad Pro 11 <br> <img src="assets/documentation/ipadpro-home.png" height=400> | 834 | 1194 |

#### Laptops and Desktops
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| MacBook Air 13' <br> <img src="assets/documentation/macbook-home.png" height=400> | 1280 | 800 |
| Dell Latitude <br> <img src="assets/documentation/dell-home.png" height=400> | 1440 | 809 |
| iMac 24' <br> <img src="assets/documentation/imac-home.png" height=400>  | 2048 | 1142 |


---

### Login Screen

#### Mobiles
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPhone 5 <br> <img src="assets/documentation/iphone5-login.png" height=400> | 320 | 568 |
| iPhone 13 <br> <img src="assets/documentation/iphone13-login.png" height=400> | 390 | 844 |
| Samsung S20 <br> <img src="assets/documentation/samsung-s20-signin.png" height=400> | 360 | 800 |
| OnePlus Nord 2 <br> <img src="assets/documentation/oneplus-signin.png" height=400> | 412 | 915 |

#### Tablets
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPad Mini <br> <img src="assets/documentation/ipadmini-signin.png" height=400> | 768 | 1024 |
| Galaxy Tab S7 <br> <img src="assets/documentation/galaxytab-signin.png" height=400> | 800 | 1280 |
| iPad Pro 11 <br> <img src="assets/documentation/ipadpro-signin.png" height=400> | 834 | 1194 |

#### Laptops and Desktops
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| MacBook Air 13' <br> <img src="assets/documentation/macbook-signin.png" height=400> | 1280 | 800 |
| Dell Latitude <br> <img src="assets/documentation/dell-signin.png" height=400> | 1440 | 809 |
| iMac 24' <br> <img src="assets/documentation/imac-signin.png" height=400>  | 2048 | 1142 |

---

### Logout Screen

#### Mobiles
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPhone 5 <br> <img src="assets/documentation/iphone5-logout.png" height=400> | 320 | 568 |
| iPhone 13 <br> <img src="assets/documentation/iphone13-signout.png" height=400> | 390 | 844 |
| Samsung S20 <br> <img src="assets/documentation/samsung-s20-signout.png" height=400> | 360 | 800 |
| OnePlus Nord 2 <br> <img src="assets/documentation/oneplus-signout.png" height=400> | 412 | 915 |

#### Tablets
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPad Mini <br> <img src="assets/documentation/ipadmini-signout.png" height=400> | 768 | 1024 |
| Galaxy Tab S7 <br> <img src="assets/documentation/galaxytab-signout.png" height=400> | 800 | 1280 |
| iPad Pro 11 <br> <img src="assets/documentation/ipadpro-signout.png" height=400> | 834 | 1194 |

#### Laptops and Desktops
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| MacBook Air 13' <br> <img src="assets/documentation/macbook-signout.png" height=400> | 1280 | 800 |
| Dell Latitude <br> <img src="assets/documentation/dell-signout.png" height=400> | 1440 | 809 |
| iMac 24' <br> <img src="assets/documentation/imac-signout.png" height=400>  | 2048 | 1142 |

---

### SignUp Screen

#### Mobiles
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPhone 5 <br> <img src="assets/documentation/iphone5-signup.png" height=400> | 320 | 568 |
| iPhone 13 <br> <img src="assets/documentation/iphone13-signup.png" height=400> | 390 | 844 |
| Samsung S20 <br> <img src="assets/documentation/samsung-s20-signup.png" height=400> | 360 | 800 |
| OnePlus Nord 2 <br> <img src="assets/documentation/oneplus-signup.png" height=400> | 412 | 915 |

#### Tablets
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPad Mini <br> <img src="assets/documentation/ipadmini-signup.png" height=400> | 768 | 1024 |
| Galaxy Tab S7 <br> <img src="assets/documentation/galaxytab-signup.png" height=400> | 800 | 1280 |
| iPad Pro 11 <br> <img src="assets/documentation/ipadpro-signup.png" height=400> | 834 | 1194 |

#### Laptops and Desktops
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| MacBook Air 13' <br> <img src="assets/documentation/macbook-signup.png" height=400> | 1280 | 800 |
| Dell Latitude <br> <img src="assets/documentation/dell-signup.png" height=400> | 1440 | 809 |
| iMac 24' <br> <img src="assets/documentation/imac-signup.png" height=400>  | 2048 | 1142 |

---

### Leader Dashboard

#### Mobiles
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPhone 5 <br> <img src="assets/documentation/iphone5-leader.png" height=400> | 320 | 568 |
| iPhone 13 <br> <img src="assets/documentation/iphone13-leader.png" height=400> | 390 | 844 |
| Samsung S20 <br> <img src="assets/documentation/samsung-s20-leader-dash.png" height=400> | 360 | 800 |
| OnePlus Nord 2 <br> <img src="assets/documentation/oneplus-leader-dash.png" height=400> | 412 | 915 |

#### Tablets
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPad Mini <br> <img src="assets/documentation/ipadmini-leader-dash.png" height=400> | 768 | 1024 |
| Galaxy Tab S7 <br> <img src="assets/documentation/galaxytab-leader-dash.png" height=400> | 800 | 1280 |
| iPad Pro 11 <br> <img src="assets/documentation/ipadpro-leader-dash.png" height=400> | 834 | 1194 |

#### Laptops and Desktops
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| MacBook Air 13' <br> <img src="assets/documentation/macbook-leader-dash.png" height=400> | 1280 | 800 |
| Dell Latitude <br> <img src="assets/documentation/dell-leader-dash.png" height=400> | 1440 | 809 |
| iMac 24' <br> <img src="assets/documentation/imac-leader-dash.png" height=400>  | 2048 | 1142 |

---

### Scout Dashboard

#### Mobiles
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPhone 5 <br> <img src="assets/documentation/iphone5-scout-dash.png" height=400> | 320 | 568 |
| iPhone 13 <br> <img src="assets/documentation/iphone13-scout-dash.png" height=400> | 390 | 844 |
| Samsung S20 <br> <img src="assets/documentation/samsung-s20-scout-dash.png" height=400> | 360 | 800 |
| OnePlus Nord 2 <br> <img src="assets/documentation/oneplus-scout-dash.png" height=400> | 412 | 915 |

#### Tablets
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPad Mini <br> <img src="assets/documentation/ipadmini-scout-dash.png" height=400> | 768 | 1024 |
| Galaxy Tab S7 <br> <img src="assets/documentation/galaxytab-scout-dash.png" height=400> | 800 | 1280 |
| iPad Pro 11 <br> <img src="assets/documentation/ipadpro-scout-dash.png" height=400> | 834 | 1194 |

#### Laptops and Desktops
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| MacBook Air 13' <br> <img src="assets/documentation/macbook-scout-dash.png" height=400> | 1280 | 800 |
| Dell Latitude <br> <img src="assets/documentation/dell-scout-dash.png" height=400> | 1440 | 809 |
| iMac 24' <br> <img src="assets/documentation/imac-scout-dash.png" height=400>  | 2048 | 1142 |

---

### Badges

#### Mobiles
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPhone 5 <br> <img src="assets/documentation/iphone5-badges.png" height=400> | 320 | 568 |
| iPhone 13 <br> <img src="assets/documentation/iphone13-badges.png" height=400> | 390 | 844 |
| Samsung S20 <br> <img src="assets/documentation/samsung-s20-badges.png" height=400> | 360 | 800 |
| OnePlus Nord 2 <br> <img src="assets/documentation/oneplus-badges.png" height=400> | 412 | 915 |

#### Tablets
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPad Mini <br> <img src="assets/documentation/ipadmini-badges.png" height=400> | 768 | 1024 |
| Galaxy Tab S7 <br> <img src="assets/documentation/galaxytab-badges.png" height=400> | 800 | 1280 |
| iPad Pro 11 <br> <img src="assets/documentation/ipadpro-badges.png" height=400> | 834 | 1194 |

#### Laptops and Desktops
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| MacBook Air 13' <br> <img src="assets/documentation/macbook-badges.png" height=400> | 1280 | 800 |
| Dell Latitude <br> <img src="assets/documentation/dell-badges.png" height=400> | 1440 | 809 |
| iMac 24' <br> <img src="assets/documentation/imac-badges.png" height=400>  | 2048 | 1142 |

---

### Badge Detail

#### Mobiles
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPhone 5 <br> <img src="assets/documentation/iphone5-badge-detail.png" height=400> | 320 | 568 |
| iPhone 13 <br> <img src="assets/documentation/iphone13-badge-detail.png" height=400> | 390 | 844 |
| Samsung S20 <br> <img src="assets/documentation/samsung-s20-badge-detail.png" height=400> | 360 | 800 |
| OnePlus Nord 2 <br> <img src="assets/documentation/oneplus-badge-detail.png" height=400> | 412 | 915 |

#### Tablets
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPad Mini <br> <img src="assets/documentation/ipadmini-badge-detail.png" height=400> | 768 | 1024 |
| Galaxy Tab S7 <br> <img src="assets/documentation/galaxytab-badge-detail.png" height=400> | 800 | 1280 |
| iPad Pro 11 <br> <img src="assets/documentation/ipadpro-badge-detail.png" height=400> | 834 | 1194 |

#### Laptops and Desktops
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| MacBook Air 13' <br> <img src="assets/documentation/macbook-badge-detail.png" height=400> | 1280 | 800 |
| Dell Latitude <br> <img src="assets/documentation/dell-badge-detail.png" height=400> | 1440 | 809 |
| iMac 24' <br> <img src="assets/documentation/imac-badge-detail.png" height=400>  | 2048 | 1142 |

---

### Add Badge

#### Mobiles
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPhone 5 <br> <img src="assets/documentation/iphone5-add-badge.png" height=400> | 320 | 568 |
| iPhone 13 <br> <img src="assets/documentation/iphone13-add-badge.png" height=400> | 390 | 844 |
| Samsung S20 <br> <img src="assets/documentation/samsung-s20-add-badge.png" height=400> | 360 | 800 |
| OnePlus Nord 2 <br> <img src="assets/documentation/oneplus-add-badge.png" height=400> | 412 | 915 |

#### Tablets
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPad Mini <br> <img src="assets/documentation/ipadmini-add-badge.png" height=400> | 768 | 1024 |
| Galaxy Tab S7 <br> <img src="assets/documentation/galaxytab-add-badge.png" height=400> | 800 | 1280 |
| iPad Pro 11 <br> <img src="assets/documentation/ipadpro-add-badge.png" height=400> | 834 | 1194 |

#### Laptops and Desktops
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| MacBook Air 13' <br> <img src="assets/documentation/macbook-add-badge.png" height=400> | 1280 | 800 |
| Dell Latitude <br> <img src="assets/documentation/dell-add-badge.png" height=400> | 1440 | 809 |
| iMac 24' <br> <img src="assets/documentation/imac-add-badge.png" height=400>  | 2048 | 1142 |

---

### Edit Badge

#### Mobiles
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPhone 5 <br> <img src="assets/documentation/iphone5-edit-badge.png" height=400> | 320 | 568 |
| iPhone 13 <br> <img src="assets/documentation/iphone13-edit-badge.png" height=400> | 390 | 844 |
| Samsung S20 <br> <img src="assets/documentation/samsung-s20-edit-badge.png" height=400> | 360 | 800 |
| OnePlus Nord 2 <br> <img src="assets/documentation/oneplus-edit-badge.png" height=400> | 412 | 915 |

#### Tablets
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPad Mini <br> <img src="assets/documentation/ipadmini-edit-badge.png" height=400> | 768 | 1024 |
| Galaxy Tab S7 <br> <img src="assets/documentation/galaxytab-edit-badge.png" height=400> | 800 | 1280 |
| iPad Pro 11 <br> <img src="assets/documentation/ipadpro-edit-badge.png" height=400> | 834 | 1194 |

#### Laptops and Desktops
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| MacBook Air 13' <br> <img src="assets/documentation/macbook-edit-badge.png" height=400> | 1280 | 800 |
| Dell Latitude <br> <img src="assets/documentation/dell-edit-badge.png" height=400> | 1440 | 809 |
| iMac 24' <br> <img src="assets/documentation/imac-edit-badge.png" height=400>  | 2048 | 1142 |
 
---

### Blog

#### Mobiles
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPhone 5 <br> <img src="assets/documentation/iphone5-blog.png" height=400> | 320 | 568 |
| iPhone 13 <br> <img src="assets/documentation/iphone13-blog.png" height=400> | 390 | 844 |
| Samsung S20 <br> <img src="assets/documentation/samsung-s20-blog.png" height=400> | 360 | 800 |
| OnePlus Nord 2 <br> <img src="assets/documentation/oneplus-blog.png" height=400> | 412 | 915 |

#### Tablets
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPad Mini <br> <img src="assets/documentation/ipadmini-blog.png" height=400> | 768 | 1024 |
| Galaxy Tab S7 <br> <img src="assets/documentation/galaxytab-blog.png" height=400> | 800 | 1280 |
| iPad Pro 11 <br> <img src="assets/documentation/ipadpro-blog.png" height=400> | 834 | 1194 |

#### Laptops and Desktops
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| MacBook Air 13' <br> <img src="assets/documentation/macbook-blog.png" height=400> | 1280 | 800 |
| Dell Latitude <br> <img src="assets/documentation/dell-blog.png" height=400> | 1440 | 809 |
| iMac 24' <br> <img src="assets/documentation/imac-blog.png" height=400>  | 2048 | 1142 |

---

### Blog Post

#### Mobiles
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPhone 5 <br> <img src="assets/documentation/iphone5-blog-post.png" height=400> | 320 | 568 |
| iPhone 13 <br> <img src="assets/documentation/iphone13-blog-post.png" height=400> | 390 | 844 |
| Samsung S20 <br> <img src="assets/documentation/samsung-s20-blog-post.png" height=400> | 360 | 800 |
| OnePlus Nord 2 <br> <img src="assets/documentation/oneplus-blog-post.png" height=400> | 412 | 915 |

#### Tablets
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPad Mini <br> <img src="assets/documentation/ipadmini-blog-post.png" height=400> | 768 | 1024 |
| Galaxy Tab S7 <br> <img src="assets/documentation/galaxytab-blog-post.png" height=400> | 800 | 1280 |
| iPad Pro 11 <br> <img src="assets/documentation/ipadpro-blog-post.png" height=400> | 834 | 1194 |

#### Laptops and Desktops
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| MacBook Air 13' <br> <img src="assets/documentation/macbook-blog-post.png" height=400> | 1280 | 800 |
| Dell Latitude <br> <img src="assets/documentation/dell-blog-post.png" height=400> | 1440 | 809 |
| iMac 24' <br> <img src="assets/documentation/imac-blog-post.png" height=400>  | 2048 | 1142 |

---

### Create Post

#### Mobiles
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPhone 5 <br> <img src="assets/documentation/iphone5-create-post.png" height=400> | 320 | 568 |
| iPhone 13 <br> <img src="assets/documentation/iphone13-create-post.png" height=400> | 390 | 844 |
| Samsung S20 <br> <img src="assets/documentation/samsung-s20-create-post.png" height=400> | 360 | 800 |
| OnePlus Nord 2 <br> <img src="assets/documentation/oneplus-create-post.png" height=400> | 412 | 915 |

#### Tablets
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPad Mini <br> <img src="assets/documentation/ipadmini-create-post.png" height=400> | 768 | 1024 |
| Galaxy Tab S7 <br> <img src="assets/documentation/galaxytab-create-post.png" height=400> | 800 | 1280 |
| iPad Pro 11 <br> <img src="assets/documentation/ipadpro-create-post.png" height=400> | 834 | 1194 |

#### Laptops and Desktops
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| MacBook Air 13' <br> <img src="assets/documentation/macbook-create-post.png" height=400> | 1280 | 800 |
| Dell Latitude <br> <img src="assets/documentation/dell-create-post.png" height=400> | 1440 | 809 |
| iMac 24' <br> <img src="assets/documentation/imac-create-post.png" height=400>  | 2048 | 1142 |

---

### Manage Scouts

#### Mobiles
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPhone 5 <br> <img src="assets/documentation/iphone5-manage-scouts.png" height=400> | 320 | 568 |
| iPhone 13 <br> <img src="assets/documentation/iphone13-manage-scouts.png" height=400> | 390 | 844 |
| Samsung S20 <br> <img src="assets/documentation/samsung-s20-manage-scouts.png" height=400> | 360 | 800 |
| OnePlus Nord 2 <br> <img src="assets/documentation/oneplus-manage-scouts.png" height=400> | 412 | 915 |

#### Tablets
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| iPad Mini <br> <img src="assets/documentation/ipadmini-manage-scouts.png" height=400> | 768 | 1024 |
| Galaxy Tab S7 <br> <img src="assets/documentation/galaxytab-manage-scouts.png" height=400> | 800 | 1280 |
| iPad Pro 11 <br> <img src="assets/documentation/ipadpro-manage-scouts.png" height=400> | 834 | 1194 |

#### Laptops and Desktops
| Device | Screen Width(px) | Screen Height (px)|
| --- | --- | --- |
| MacBook Air 13' <br> <img src="assets/documentation/macbook-manage-scouts.png" height=400> | 1280 | 800 |
| Dell Latitude <br> <img src="assets/documentation/dell-manage-scouts.png" height=400> | 1440 | 809 |
| iMac 24' <br> <img src="assets/documentation/imac-manage-scouts.png" height=400>  | 2048 | 1142 |

---

<a id=defensive-programming></a>

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Screen Clip |
| --- | --- | --- | --- | --- |
| Nav links | | | | |
| | Click on Dashboard link in navbar | Redirection to Dashboard | Pass | <img src="assets/documentation/nav-dashboard-link.gif" alt="NavBar Dashboard Link gif" width=700> |
| | Click on Badges link in navbar | Redirection to Badges page | Pass | <img src="assets/documentation/nav-badges-link.gif" alt="NavBar Badges Link gif" width=700> |
| | Click on Blog link in navbar | Redirection to Blog page | Pass | <img src="assets/documentation/nav-blog-link.gif" alt="NavBar Blog Link gif" width=700> |
| | Click on Manage Scouts link in navbar | Redirection to Manage Scouts page | Pass | <img src="assets/documentation/nav-manage-scouts-link.gif" alt="NavBar Manage Scouts Link gif" width=700> |
| | Click on Logout link in navbar | Redirection to Logout page | Pass | <img src="assets/documentation/nav-logout-link.gif" alt="NavBar Logout Link gif" width=700> |
| Home page | | | | |
| | Click on Login button | Redirection to Login page | Pass | <img src="assets/documentation/home-login-button.gif" alt="Home Page Login Button gif" width=700> |
| | Click on Sign up button | Redirection to that itinerary's details page | Pass | <img src="assets/documentation/home-signup-button.gif" alt="Home Page Signup Button gif" width=700> |
| Dashboard (Leader) | | | | |
| | Click on Edit Badge button  | Redirection to edit badge form page | Pass | <img src="assets/documentation/leader-edit-badge-button.gif" alt="Edit Badge Button gif" width=700> |
| | Click on Delete Badge button  | Delete confirmation modal appears at the top of the screen | Pass | <img src="assets/documentation/leader-delete-badge-button.gif" alt="Delete Badge Button Gif" width=700> |
| | Click on Add Badge button  | Redirection to Add badge form page | Pass | <img src="assets/documentation/leader-addbadge-button.gif" alt="Add Badge Button gif" width=700> |
| | Click Approve button | Request is removed and scout receives earned badge | Pass | <img src="assets/documentation/request-approved-badge-earned.gif" alt="Approve Request gif" width=700> |
| | Click Reject button | Request is removed and request badge button is re-enabled for scout | Pass | <img src="assets/documentation/request-rejected-button-enabled.gif" alt="Reject request gif" width=700> |
| Dashboard (Scout) | | | | |
| | Click on Feature button  | Adds the Badge to the featured section of the dashboard | Pass | <img src="assets/documentation/feature-button.gif" alt="Feature Button gif" width=700> |
| | Click on Unfeature button  | Removes the Badge from the feature section of the dashboard | Pass | <img src="assets/documentation/unfeature-button.gif" alt="Unfeature Button gif" width=700> |
| Delete Confirmation Modal | | | | |
| | Click on Delete button  | Deletes Badge from database and redirection to badges page | Pass | <img src="assets/documentation/deletebadge-modal-delete-button.gif" alt="Delete badge Modal Delete Button gif" width=700> |
| | Click on Close button  | Closes Delete Confirmation Modal | Pass | <img src="assets/documentation/deletebadge-modal-close-button.gif" alt="Delete Badge Modal Close Button gif " width=700> |
| Badges Page | | | | |
| | Click Badge Link | Redirect to badge detail page | Pass | <img src="assets/documentation/badges-badge-link.gif" alt="Badge detail Link gif" width=700> |
| Badges Detail Page (Only Scouts can view this button) | | | | |
| | Click Request Badge Button | Button is disabled and a Leader will receive the request | Pass | <img src="assets/documentation/request-badge-request-received.gif" alt="Request Badge gif" width=700> |
| Blog Page | | | | |
| | Click on Blog Link | Redirect to Blog Post page | Pass | <img src="assets/documentation/blog-blog-link.gif" alt="Link to Blog gif" width=700>  |
| | Click on Create Post button | Redirect to Create Post Form page | Pass | <img src="assets/documentation/blog-create-post-button.gif" alt="Create Post gif" width=700>  |
| | Click on Next Button| Redirect to Next Page of Posts | Pass | <img src="assets/documentation/next-button.gif" alt="Next page button gif" width=700>  |
| | Click on Prev Button | Redirect to Previous Page of Posts | Pass | <img src="assets/documentation/prev-button.gif" alt="Previous page button gif" width=700> |
| Blog Post Page | | | | |
| | Click on Submit button | Text is uploaded to the page under comments section | Pass | <img src="assets/documentation/blog-post-comment-submit.gif" alt="Request Badge gif" width=700> |
| | Click on Delete Button | Comment Deletion Modal appears at the top of the screen | Pass | <img src="assets/documentation/comment-deletion-modal.gif" alt="Comment Deletion Modal gif" width=700> |
| | Click on Close Button | Closes Comment Deletion Modal | Pass | <img src="assets/documentation/comment-modal-close-button.gif" alt="Comment Modal Close Button gif" width=700> |
| | Click on Delete button (inside modal) | Deletes the submitted text from the comments section | Pass | <img src="assets/documentation/comment-modal-delete-button.gif" alt="Request Badge gif" width=700> |
| | Click on Edit Button | Previously entered text is displayed in the text field | Pass | <img src="assets/documentation/edit-comment.gif" alt="Edit comment gif" width=700> |
| | Click on Update Button | Updated text field replaces previous comment | Pass | <img src="assets/documentation/submit-new-comment.gif" alt="Updating a comment gif" width=700> |
| Create Post Page | | | | |
| | Enter Text into provided fields (Title, content, excerpt) | Entered Text is displayed correctly | Pass | <img src="assets/documentation/post-creation.gif" alt="Creating new post" width=700> |
| | Click Post Button | Post is uploaded to Blog Page and redirect to Blog Page | Pass | <img src="assets/documentation/create-post-button.gif" alt="Post button gif" width=700> |
| Manage Scouts Page | | | | |
| | Click DropDown Button | Gives a List of Patrols inputs the selected Patrol name| Pass | <img src="assets/documentation/patrol-dropdown.gif" alt="Patrol dropdown button" width=700> |
| | Click on Save Button | Updates the users Patrol to selected input | Pass | <img src="assets/documentation/manage-scouts-save-button.gif" alt="Save patrol button" width=700> |
| Login Page | | | | |
| | Enter valid Username | Field will only accept registered users | Pass | <img src="assets/documentation/user-login.gif" alt="Username field gif" width=700> |
| | Enter valid password | Field will only accept password format | Pass | <img src="assets/documentation/password-login.gif" alt="Password field gif" width=700> |
| | Click on Sign In button | Redirects user to Dashboard | Pass | <img src="assets/documentation/signin-page-signin-button.gif" alt="Sign in Button gif" width=700> |
| | Click on Sign Up link | Redirects user to Sign Up page | Pass | <img src="assets/documentation/login-signup-link.gif" alt="SignUp Link gif" width=700> |
| Sign Up Page | | | | |
| | Enter valid Username | Field will only accept username format | Pass | <img src="assets/documentation/username-signup.gif" alt="Username field gif" width=700> |
| | Enter valid password (twice) | Field will only accept password format | Pass | <img src="assets/documentation/password-signup.gif" alt="Password field gif" width=700> |
| | Click Sign Up button | Redirects user to Dashboard | Pass | <img src="assets/documentation/signup-signup-button.gif" alt="SignUp Button gif" width=700> |
| | Click Log in link | Redirects user to Log In page | Pass | <img src="assets/documentation/signup-login-link.gif" alt="Login Link gif" width=700> |
| | Choose Role from Dropdown | Gives the choice of 'Scout' or 'Leader' | Pass | <img src="assets/documentation/role-choice.gif" width=700> |
| Log Out Page | | | | |
| | Click Sign Out button | Logs out user, Redirects user to Home page | Pass | <img src="assets/documentation/signout-button.gif" width=700> |

---

<a id=user-story-testing></a>

## User Story Testing


| User Stories | How were they achieved? |
| ------ | -------------------------- |
| As a User I would like to be able to Login so that I can view my currently owned badges. | This has been achieved by adding a signup form that users can create an account with and a login page which the user can enter their new username and password into in order to access the sites full features. |
| As a Scout I would like to see the current status of a badge request I made so that I can see once it has been approved or not.| Once the User sends a badge request the button becomes disabled and the name changes to 'Pending request' this is to allow the user to know that the request has been sent off. Once approved by a Leader the badge is automatically added to their earned badges in the dashboard so they know that the request was approved. However if it was rejected then the badge request button becomes usable again for the Scout to make another request once they have met all the requirements. |
| As a Scout, I want to be able to register for an account so that I can track my current progress and view my earned badges. | This is achieved by filling out the signup form mentioned earlier. |
| I want users to see specific features based on their role as either a 'Scout' or 'Leader' so that they have appropriate access. | Role-Based Access Control(RBAC) features were used to ensure that only Leaders can access the 'Manage Scout' tab and the functionality to add/edit or delete badges in the database. This was achieved by using if functions such as 'if user.role == 'leader'. These functions prevented users with the role of scout from being able to access these features. |
| As a Scout I would like to be able to request a badge that I believe to be completed.| When viewing a specific badge from the list of badges, users with the role of 'scout' are able to see a button at the bottom labelled 'request badge' once they press this button the request for that specific badge is sent to the leaders for them to approve or reject. |
| As a Leader I would like to be able to approve or disapprove badge requests made by my scouts based on how much of the requirements have been met. | Once a request has been sent by a Scout the Leaders will receive the request with an option to approve or reject it within the 'Pending Badge Requests' section. |
| As a User I would like to be able to Logout of my session manually so that my account remains secure. | A clearly labelled navigation link 'Signout' can be used to access the signout page where the user can end their session and prevent other people from accessing their account. |
| As a Scout I would like the option to feature some of my earned badges on my dashboard as a way of showing my progress as a scout to myself and people who view my profile. | Underneath all earned badges in a Scouts dashboard is a button labelled 'Feature', using this button adds the badge to the 'Featured Badges' section and the buttons label changes to 'Unfeature'. If the button is used while it says 'Unfeature' then the selected badge is removed from the featured badge section. |
| As a Leader I would like to be able to manage the currently shown badges in the badge list and have an option to add new badges with the name, description and requirements . So that the list is kept up to date.| From the Leader Dashboard the users can edit or delete badges that are shown in the 'Manage Badges' section. Additionally they can use the 'Add Badge' button which redirects them to the 'Create badge' form that can be filled out with a name, description, image and requirements. If a badge requires more than the default requirements the 'Add requirement' button can be used to add another input text field. |
| As a Leader I would like to be able to manage the scouts that register to the site so that I can add them to patrols. | From the 'Manage Scouts' tab (Available only to Leaders) is a table with names of current scouts that have registered, their currently assigned patrol (labelled as 'unassigned' if none has been selected) and a dropdown button that displays a list of Patrol names. The Leader can select the new patrol name from the dropdown list and click the 'Save' button to update the Scouts assigned patrol. |
| As a user I would like to be able to create a post in a forum page of some kind so that I can ask and answer questions. | The 'Blog' page is this website's forum page where a list of posts are displayed with links that once clicked will redirect the user to the specific post. If the user wishes to create their own post they can select the 'Create Post' button near the bottom of the page which redirects them to the 'Create Post' form that can then be filled out with a Title, content, and an excerpt(description). Once the user then selects the 'Post' Button they are redirected to the 'Blog' page where they will see their newly created post.

---

<a id=bugs></a>

## Bugs

No major bugs were identified during testing.
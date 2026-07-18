# UX Guidelines — referencia transversal

99 reglas prácticas de UX importadas de UI UX Pro Max (catálogo `ux-guidelines.csv`, 2026-04-13). Aplicables a cualquier preset de adri-style.

**Cómo usarlas:** consultar antes de finalizar una página. Cada regla tiene severidad — atender las `Critical` y `High` siempre, las `Medium` cuando aporten, las `Low` cuando haya margen.

## Índice por categoría

- [AI Interaction](#ai-interaction) — 3 reglas
- [Accessibility](#accessibility) — 11 reglas
- [Animation](#animation) — 8 reglas
- [Content](#content) — 4 reglas
- [Data Entry](#data-entry) — 1 reglas
- [Feedback](#feedback) — 6 reglas
- [Forms](#forms) — 10 reglas
- [Interaction](#interaction) — 8 reglas
- [Layout](#layout) — 7 reglas
- [Navigation](#navigation) — 6 reglas
- [Onboarding](#onboarding) — 1 reglas
- [Performance](#performance) — 8 reglas
- [Responsive](#responsive) — 8 reglas
- [Search](#search) — 2 reglas
- [Spatial UI](#spatial-ui) — 2 reglas
- [Sustainability](#sustainability) — 2 reglas
- [Touch](#touch) — 6 reglas
- [Typography](#typography) — 6 reglas

## AI Interaction

### 92. Disclaimer 🟠 *High*

Users need to know they talk to AI

**Do:** Clearly label AI generated content
**Don't:** Present AI as human

```
/* ✓ */ AI Assistant label
```
```
/* ✗ */ Fake human name without label
```

---

### 93. Streaming 🟡 *Medium*

Waiting for full text is slow

**Do:** Stream text response token by token
**Don't:** Show loading spinner for 10s+

```
/* ✓ */ Typewriter effect
```
```
/* ✗ */ Spinner until 100% complete
```

---

### 98. Feedback Loop ⚪ *Low*

AI needs user feedback to improve

**Do:** Thumps up/down or 'Regenerate'
**Don't:** Static output only

```
/* ✓ */ Feedback component
```
```
/* ✗ */ Read-only text
```

---

## Accessibility

### 36. Color Contrast 🟠 *High*

Text must be readable against background

**Do:** Minimum 4.5:1 ratio for normal text
**Don't:** Low contrast text

```
/* ✓ */ #333 on white (7:1)
```
```
/* ✗ */ #999 on white (2.8:1)
```

---

### 37. Color Only 🟠 *High*

Don't convey information by color alone

**Do:** Use icons/text in addition to color
**Don't:** Red/green only for error/success

```
/* ✓ */ Red text + error icon
```
```
/* ✗ */ Red border only for error
```

---

### 38. Alt Text 🟠 *High*

Images need text alternatives

**Do:** Descriptive alt text for meaningful images
**Don't:** Empty or missing alt attributes

```
/* ✓ */ alt='Dog playing in park'
```
```
/* ✗ */ alt='' for content images
```

---

### 39. Heading Hierarchy 🟡 *Medium*

Screen readers use headings for navigation

**Do:** Use sequential heading levels h1-h6
**Don't:** Skip heading levels or misuse for styling

```
/* ✓ */ h1 then h2 then h3
```
```
/* ✗ */ h1 then h4
```

---

### 40. ARIA Labels 🟠 *High*

Interactive elements need accessible names

**Do:** Add aria-label for icon-only buttons
**Don't:** Icon buttons without labels

```
/* ✓ */ aria-label='Close menu'
```
```
/* ✗ */ <button><Icon/></button>
```

---

### 41. Keyboard Navigation 🟠 *High*

All functionality accessible via keyboard

**Do:** Tab order matches visual order
**Don't:** Keyboard traps or illogical tab order

```
/* ✓ */ tabIndex for custom order
```
```
/* ✗ */ Unreachable elements
```

---

### 42. Screen Reader 🟡 *Medium*

Content should make sense when read aloud

**Do:** Use semantic HTML and ARIA properly
**Don't:** Div soup with no semantics

```
/* ✓ */ <nav> <main> <article>
```
```
/* ✗ */ <div> for everything
```

---

### 43. Form Labels 🟠 *High*

Inputs must have associated labels

**Do:** Use label with for attribute or wrap input
**Don't:** Placeholder-only inputs

```
/* ✓ */ <label for='email'>
```
```
/* ✗ */ placeholder='Email' only
```

---

### 44. Error Messages 🟠 *High*

Error messages must be announced

**Do:** Use aria-live or role=alert for errors
**Don't:** Visual-only error indication

```
/* ✓ */ role='alert'
```
```
/* ✗ */ Red border only
```

---

### 45. Skip Links 🟡 *Medium*

Allow keyboard users to skip navigation

**Do:** Provide skip to main content link
**Don't:** No skip link on nav-heavy pages

```
/* ✓ */ Skip to main content link
```
```
/* ✗ */ 100 tabs to reach content
```

---

### 99. Motion Sensitivity 🟠 *High*

Parallax/Scroll-jacking causes nausea

**Do:** Respect prefers-reduced-motion
**Don't:** Force scroll effects

```
/* ✓ */ @media (prefers-reduced-motion)
```
```
/* ✗ */ ScrollTrigger.create()
```

---

## Animation

### 7. Excessive Motion 🟠 *High*

Too many animations cause distraction and motion sickness

**Do:** Animate 1-2 key elements per view maximum
**Don't:** Animate everything that moves

```
/* ✓ */ Single hero animation
```
```
/* ✗ */ animate-bounce on 5+ elements
```

---

### 8. Duration Timing 🟡 *Medium*

Animations should feel responsive not sluggish

**Do:** Use 150-300ms for micro-interactions
**Don't:** Use animations longer than 500ms for UI

```
/* ✓ */ transition-all duration-200
```
```
/* ✗ */ duration-1000
```

---

### 9. Reduced Motion 🟠 *High*

Respect user's motion preferences

**Do:** Check prefers-reduced-motion media query
**Don't:** Ignore accessibility motion settings

```
/* ✓ */ @media (prefers-reduced-motion: reduce)
```
```
/* ✗ */ No motion query check
```

---

### 10. Loading States 🟠 *High*

Show feedback during async operations

**Do:** Use skeleton screens or spinners
**Don't:** Leave UI frozen with no feedback

```
/* ✓ */ animate-pulse skeleton
```
```
/* ✗ */ Blank screen while loading
```

---

### 11. Hover vs Tap 🟠 *High*

Hover effects don't work on touch devices

**Do:** Use click/tap for primary interactions
**Don't:** Rely only on hover for important actions

```
/* ✓ */ onClick handler
```
```
/* ✗ */ onMouseEnter only
```

---

### 12. Continuous Animation 🟡 *Medium*

Infinite animations are distracting

**Do:** Use for loading indicators only
**Don't:** Use for decorative elements

```
/* ✓ */ animate-spin on loader
```
```
/* ✗ */ animate-bounce on icons
```

---

### 13. Transform Performance 🟡 *Medium*

Some CSS properties trigger expensive repaints

**Do:** Use transform and opacity for animations
**Don't:** Animate width/height/top/left properties

```
/* ✓ */ transform: translateY()
```
```
/* ✗ */ top: 10px animation
```

---

### 14. Easing Functions ⚪ *Low*

Linear motion feels robotic

**Do:** Use ease-out for entering ease-in for exiting
**Don't:** Use linear for UI transitions

```
/* ✓ */ ease-out
```
```
/* ✗ */ linear
```

---

## Content

### 84. Truncation 🟡 *Medium*

Handle long content gracefully

**Do:** Truncate with ellipsis and expand option
**Don't:** Overflow or broken layout

```
/* ✓ */ line-clamp-2 with expand
```
```
/* ✗ */ Overflow or cut off
```

---

### 85. Date Formatting ⚪ *Low*

Use locale-appropriate date formats

**Do:** Use relative or locale-aware dates
**Don't:** Ambiguous date formats

```
/* ✓ */ 2 hours ago or locale format
```
```
/* ✗ */ 01/02/03
```

---

### 86. Number Formatting ⚪ *Low*

Format large numbers for readability

**Do:** Use thousand separators or abbreviations
**Don't:** Long unformatted numbers

```
/* ✓ */ 1.2K or 1,234
```
```
/* ✗ */ 1234567
```

---

### 87. Placeholder Content ⚪ *Low*

Show realistic placeholders during dev

**Do:** Use realistic sample data
**Don't:** Lorem ipsum everywhere

```
/* ✓ */ Real sample content
```
```
/* ✗ */ Lorem ipsum
```

---

## Data Entry

### 91. Bulk Actions ⚪ *Low*

Editing one by one is tedious

**Do:** Allow multi-select and bulk edit
**Don't:** Single row actions only

```
/* ✓ */ Checkbox column + Action bar
```
```
/* ✗ */ Repeated actions per row
```

---

## Feedback

### 78. Loading Indicators 🟠 *High*

Show system status during waits

**Do:** Show spinner/skeleton for operations > 300ms
**Don't:** No feedback during loading

```
/* ✓ */ Skeleton or spinner
```
```
/* ✗ */ Frozen UI
```

---

### 79. Empty States 🟡 *Medium*

Guide users when no content exists

**Do:** Show helpful message and action
**Don't:** Blank empty screens

```
/* ✓ */ No items yet. Create one!
```
```
/* ✗ */ Empty white space
```

---

### 80. Error Recovery 🟡 *Medium*

Help users recover from errors

**Do:** Provide clear next steps
**Don't:** Error without recovery path

```
/* ✓ */ Try again button + help link
```
```
/* ✗ */ Error message only
```

---

### 81. Progress Indicators 🟡 *Medium*

Show progress for multi-step processes

**Do:** Step indicators or progress bar
**Don't:** No indication of progress

```
/* ✓ */ Step 2 of 4 indicator
```
```
/* ✗ */ No step information
```

---

### 82. Toast Notifications 🟡 *Medium*

Transient messages for non-critical info

**Do:** Auto-dismiss after 3-5 seconds
**Don't:** Toasts that never disappear

```
/* ✓ */ Auto-dismiss toast
```
```
/* ✗ */ Persistent toast
```

---

### 83. Confirmation Messages 🟡 *Medium*

Confirm successful actions

**Do:** Brief success message
**Don't:** Silent success

```
/* ✓ */ Saved successfully toast
```
```
/* ✗ */ No confirmation
```

---

## Forms

### 54. Input Labels 🟠 *High*

Every input needs a visible label

**Do:** Always show label above or beside input
**Don't:** Placeholder as only label

```
/* ✓ */ <label>Email</label><input>
```
```
/* ✗ */ placeholder='Email' only
```

---

### 55. Error Placement 🟡 *Medium*

Errors should appear near the problem

**Do:** Show error below related input
**Don't:** Single error message at top of form

```
/* ✓ */ Error under each field
```
```
/* ✗ */ All errors at form top
```

---

### 56. Inline Validation 🟡 *Medium*

Validate as user types or on blur

**Do:** Validate on blur for most fields
**Don't:** Validate only on submit

```
/* ✓ */ onBlur validation
```
```
/* ✗ */ Submit-only validation
```

---

### 57. Input Types 🟡 *Medium*

Use appropriate input types

**Do:** Use email tel number url etc
**Don't:** Text input for everything

```
/* ✓ */ type='email'
```
```
/* ✗ */ type='text' for email
```

---

### 58. Autofill Support 🟡 *Medium*

Help browsers autofill correctly

**Do:** Use autocomplete attribute properly
**Don't:** Block or ignore autofill

```
/* ✓ */ autocomplete='email'
```
```
/* ✗ */ autocomplete='off' everywhere
```

---

### 59. Required Indicators 🟡 *Medium*

Mark required fields clearly

**Do:** Use asterisk or (required) text
**Don't:** No indication of required fields

```
/* ✓ */ * required indicator
```
```
/* ✗ */ Guess which are required
```

---

### 60. Password Visibility 🟡 *Medium*

Let users see password while typing

**Do:** Toggle to show/hide password
**Don't:** No visibility toggle

```
/* ✓ */ Show/hide password button
```
```
/* ✗ */ Password always hidden
```

---

### 61. Submit Feedback 🟠 *High*

Confirm form submission status

**Do:** Show loading then success/error state
**Don't:** No feedback after submit

```
/* ✓ */ Loading -> Success message
```
```
/* ✗ */ Button click with no response
```

---

### 62. Input Affordance 🟡 *Medium*

Inputs should look interactive

**Do:** Use distinct input styling
**Don't:** Inputs that look like plain text

```
/* ✓ */ Border/background on inputs
```
```
/* ✗ */ Borderless inputs
```

---

### 63. Mobile Keyboards 🟡 *Medium*

Show appropriate keyboard for input type

**Do:** Use inputmode attribute
**Don't:** Default keyboard for all inputs

```
/* ✓ */ inputmode='numeric'
```
```
/* ✗ */ Text keyboard for numbers
```

---

## Interaction

### 28. Focus States 🟠 *High*

Keyboard users need visible focus indicators

**Do:** Use visible focus rings on interactive elements
**Don't:** Remove focus outline without replacement

```
/* ✓ */ focus:ring-2 focus:ring-blue-500
```
```
/* ✗ */ outline-none without alternative
```

---

### 29. Hover States 🟡 *Medium*

Visual feedback on interactive elements

**Do:** Change cursor and add subtle visual change
**Don't:** No hover feedback on clickable elements

```
/* ✓ */ hover:bg-gray-100 cursor-pointer
```
```
/* ✗ */ No hover style
```

---

### 30. Active States 🟡 *Medium*

Show immediate feedback on press/click

**Do:** Add pressed/active state visual change
**Don't:** No feedback during interaction

```
/* ✓ */ active:scale-95
```
```
/* ✗ */ No active state
```

---

### 31. Disabled States 🟡 *Medium*

Clearly indicate non-interactive elements

**Do:** Reduce opacity and change cursor
**Don't:** Confuse disabled with normal state

```
/* ✓ */ opacity-50 cursor-not-allowed
```
```
/* ✗ */ Same style as enabled
```

---

### 32. Loading Buttons 🟠 *High*

Prevent double submission during async actions

**Do:** Disable button and show loading state
**Don't:** Allow multiple clicks during processing

```
/* ✓ */ disabled={loading} spinner
```
```
/* ✗ */ Button clickable while loading
```

---

### 33. Error Feedback 🟠 *High*

Users need to know when something fails

**Do:** Show clear error messages near problem
**Don't:** Silent failures with no feedback

```
/* ✓ */ Red border + error message
```
```
/* ✗ */ No indication of error
```

---

### 34. Success Feedback 🟡 *Medium*

Confirm successful actions to users

**Do:** Show success message or visual change
**Don't:** No confirmation of completed action

```
/* ✓ */ Toast notification or checkmark
```
```
/* ✗ */ Action completes silently
```

---

### 35. Confirmation Dialogs 🟠 *High*

Prevent accidental destructive actions

**Do:** Confirm before delete/irreversible actions
**Don't:** Delete without confirmation

```
/* ✓ */ Are you sure modal
```
```
/* ✗ */ Direct delete on click
```

---

## Layout

### 15. Z-Index Management 🟠 *High*

Stacking context conflicts cause hidden elements

**Do:** Define z-index scale system (10 20 30 50)
**Don't:** Use arbitrary large z-index values

```
/* ✓ */ z-10 z-20 z-50
```
```
/* ✗ */ z-[9999]
```

---

### 16. Overflow Hidden 🟡 *Medium*

Hidden overflow can clip important content

**Do:** Test all content fits within containers
**Don't:** Blindly apply overflow-hidden

```
/* ✓ */ overflow-auto with scroll
```
```
/* ✗ */ overflow-hidden truncating content
```

---

### 17. Fixed Positioning 🟡 *Medium*

Fixed elements can overlap or be inaccessible

**Do:** Account for safe areas and other fixed elements
**Don't:** Stack multiple fixed elements carelessly

```
/* ✓ */ Fixed nav + fixed bottom with gap
```
```
/* ✗ */ Multiple overlapping fixed elements
```

---

### 18. Stacking Context 🟡 *Medium*

New stacking contexts reset z-index

**Do:** Understand what creates new stacking context
**Don't:** Expect z-index to work across contexts

```
/* ✓ */ Parent with z-index isolates children
```
```
/* ✗ */ z-index: 9999 not working
```

---

### 19. Content Jumping 🟠 *High*

Layout shift when content loads is jarring

**Do:** Reserve space for async content
**Don't:** Let images/content push layout around

```
/* ✓ */ aspect-ratio or fixed height
```
```
/* ✗ */ No dimensions on images
```

---

### 20. Viewport Units 🟡 *Medium*

100vh can be problematic on mobile browsers

**Do:** Use dvh or account for mobile browser chrome
**Don't:** Use 100vh for full-screen mobile layouts

```
/* ✓ */ min-h-dvh or min-h-screen
```
```
/* ✗ */ h-screen on mobile
```

---

### 21. Container Width 🟡 *Medium*

Content too wide is hard to read

**Do:** Limit max-width for text content (65-75ch)
**Don't:** Let text span full viewport width

```
/* ✓ */ max-w-prose or max-w-3xl
```
```
/* ✗ */ Full width paragraphs
```

---

## Navigation

### 1. Smooth Scroll 🟠 *High*

Anchor links should scroll smoothly to target section

**Do:** Use scroll-behavior: smooth on html element
**Don't:** Jump directly without transition

```
/* ✓ */ html { scroll-behavior: smooth; }
```
```
/* ✗ */ <a href='#section'> without CSS
```

---

### 2. Sticky Navigation 🟡 *Medium*

Fixed nav should not obscure content

**Do:** Add padding-top to body equal to nav height
**Don't:** Let nav overlap first section content

```
/* ✓ */ pt-20 (if nav is h-20)
```
```
/* ✗ */ No padding compensation
```

---

### 3. Active State 🟡 *Medium*

Current page/section should be visually indicated

**Do:** Highlight active nav item with color/underline
**Don't:** No visual feedback on current location

```
/* ✓ */ text-primary border-b-2
```
```
/* ✗ */ All links same style
```

---

### 4. Back Button 🟠 *High*

Users expect back to work predictably

**Do:** Preserve navigation history properly
**Don't:** Break browser/app back button behavior

```
/* ✓ */ history.pushState()
```
```
/* ✗ */ location.replace()
```

---

### 5. Deep Linking 🟡 *Medium*

URLs should reflect current state for sharing

**Do:** Update URL on state/view changes
**Don't:** Static URLs for dynamic content

```
/* ✓ */ Use query params or hash
```
```
/* ✗ */ Single URL for all states
```

---

### 6. Breadcrumbs ⚪ *Low*

Show user location in site hierarchy

**Do:** Use for sites with 3+ levels of depth
**Don't:** Use for flat single-level sites

```
/* ✓ */ Home > Category > Product
```
```
/* ✗ */ Only on deep nested pages
```

---

## Onboarding

### 88. User Freedom 🟡 *Medium*

Users should be able to skip tutorials

**Do:** Provide Skip and Back buttons
**Don't:** Force linear unskippable tour

```
/* ✓ */ Skip Tutorial button
```
```
/* ✗ */ Locked overlay until finished
```

---

## Performance

### 46. Image Optimization 🟠 *High*

Large images slow page load

**Do:** Use appropriate size and format (WebP)
**Don't:** Unoptimized full-size images

```
/* ✓ */ srcset with multiple sizes
```
```
/* ✗ */ 4000px image for 400px display
```

---

### 47. Lazy Loading 🟡 *Medium*

Load content as needed

**Do:** Lazy load below-fold images and content
**Don't:** Load everything upfront

```
/* ✓ */ loading='lazy'
```
```
/* ✗ */ All images eager load
```

---

### 48. Code Splitting 🟡 *Medium*

Large bundles slow initial load

**Do:** Split code by route/feature
**Don't:** Single large bundle

```
/* ✓ */ dynamic import()
```
```
/* ✗ */ All code in main bundle
```

---

### 49. Caching 🟡 *Medium*

Repeat visits should be fast

**Do:** Set appropriate cache headers
**Don't:** No caching strategy

```
/* ✓ */ Cache-Control headers
```
```
/* ✗ */ Every request hits server
```

---

### 50. Font Loading 🟡 *Medium*

Web fonts can block rendering

**Do:** Use font-display swap or optional
**Don't:** Invisible text during font load

```
/* ✓ */ font-display: swap
```
```
/* ✗ */ FOIT (Flash of Invisible Text)
```

---

### 51. Third Party Scripts 🟡 *Medium*

External scripts can block rendering

**Do:** Load non-critical scripts async/defer
**Don't:** Synchronous third-party scripts

```
/* ✓ */ async or defer attribute
```
```
/* ✗ */ <script src='...'> in head
```

---

### 52. Bundle Size 🟡 *Medium*

Large JavaScript slows interaction

**Do:** Monitor and minimize bundle size
**Don't:** Ignore bundle size growth

```
/* ✓ */ Bundle analyzer
```
```
/* ✗ */ No size monitoring
```

---

### 53. Render Blocking 🟡 *Medium*

CSS/JS can block first paint

**Do:** Inline critical CSS defer non-critical
**Don't:** Large blocking CSS files

```
/* ✓ */ Critical CSS inline
```
```
/* ✗ */ All CSS in head
```

---

## Responsive

### 64. Mobile First 🟡 *Medium*

Design for mobile then enhance for larger

**Do:** Start with mobile styles then add breakpoints
**Don't:** Desktop-first causing mobile issues

```
/* ✓ */ Default mobile + md: lg: xl:
```
```
/* ✗ */ Desktop default + max-width queries
```

---

### 65. Breakpoint Testing 🟡 *Medium*

Test at all common screen sizes

**Do:** Test at 320 375 414 768 1024 1440
**Don't:** Only test on your device

```
/* ✓ */ Multiple device testing
```
```
/* ✗ */ Single device development
```

---

### 66. Touch Friendly 🟠 *High*

Mobile layouts need touch-sized targets

**Do:** Increase touch targets on mobile
**Don't:** Same tiny buttons on mobile

```
/* ✓ */ Larger buttons on mobile
```
```
/* ✗ */ Desktop-sized targets on mobile
```

---

### 67. Readable Font Size 🟠 *High*

Text must be readable on all devices

**Do:** Minimum 16px body text on mobile
**Don't:** Tiny text on mobile

```
/* ✓ */ text-base or larger
```
```
/* ✗ */ text-xs for body text
```

---

### 68. Viewport Meta 🟠 *High*

Set viewport for mobile devices

**Do:** Use width=device-width initial-scale=1
**Don't:** Missing or incorrect viewport

```
/* ✓ */ <meta name='viewport'...>
```
```
/* ✗ */ No viewport meta tag
```

---

### 69. Horizontal Scroll 🟠 *High*

Avoid horizontal scrolling

**Do:** Ensure content fits viewport width
**Don't:** Content wider than viewport

```
/* ✓ */ max-w-full overflow-x-hidden
```
```
/* ✗ */ Horizontal scrollbar on mobile
```

---

### 70. Image Scaling 🟡 *Medium*

Images should scale with container

**Do:** Use max-width: 100% on images
**Don't:** Fixed width images overflow

```
/* ✓ */ max-w-full h-auto
```
```
/* ✗ */ width='800' fixed
```

---

### 71. Table Handling 🟡 *Medium*

Tables can overflow on mobile

**Do:** Use horizontal scroll or card layout
**Don't:** Wide tables breaking layout

```
/* ✓ */ overflow-x-auto wrapper
```
```
/* ✗ */ Table overflows viewport
```

---

## Search

### 89. Autocomplete 🟡 *Medium*

Help users find results faster

**Do:** Show predictions as user types
**Don't:** Require full type and enter

```
/* ✓ */ Debounced fetch + dropdown
```
```
/* ✗ */ No suggestions
```

---

### 90. No Results 🟡 *Medium*

Dead ends frustrate users

**Do:** Show 'No results' with suggestions
**Don't:** Blank screen or '0 results'

```
/* ✓ */ Try searching for X instead
```
```
/* ✗ */ No results found.
```

---

## Spatial UI

### 94. Gaze Hover 🟠 *High*

Elements should respond to eye tracking before pinch

**Do:** Scale/highlight element on look
**Don't:** Static element until pinch

```
/* ✓ */ hoverEffect()
```
```
/* ✗ */ onTap only
```

---

### 95. Depth Layering 🟡 *Medium*

UI needs Z-depth to separate content from environment

**Do:** Use glass material and z-offset
**Don't:** Flat opaque panels blocking view

```
/* ✓ */ .glassBackgroundEffect()
```
```
/* ✗ */ bg-white
```

---

## Sustainability

### 96. Auto-Play Video 🟡 *Medium*

Video consumes massive data and energy

**Do:** Click-to-play or pause when off-screen
**Don't:** Auto-play high-res video loops

```
/* ✓ */ playsInline muted preload='none'
```
```
/* ✗ */ autoplay loop
```

---

### 97. Asset Weight 🟡 *Medium*

Heavy 3D/Image assets increase carbon footprint

**Do:** Compress and lazy load 3D models
**Don't:** Load 50MB textures

```
/* ✓ */ Draco compression
```
```
/* ✗ */ Raw .obj files
```

---

## Touch

### 22. Touch Target Size 🟠 *High*

Small buttons are hard to tap accurately

**Do:** Minimum 44x44px touch targets
**Don't:** Tiny clickable areas

```
/* ✓ */ min-h-[44px] min-w-[44px]
```
```
/* ✗ */ w-6 h-6 buttons
```

---

### 23. Touch Spacing 🟡 *Medium*

Adjacent touch targets need adequate spacing

**Do:** Minimum 8px gap between touch targets
**Don't:** Tightly packed clickable elements

```
/* ✓ */ gap-2 between buttons
```
```
/* ✗ */ gap-0 or gap-1
```

---

### 24. Gesture Conflicts 🟡 *Medium*

Custom gestures can conflict with system

**Do:** Avoid horizontal swipe on main content
**Don't:** Override system gestures

```
/* ✓ */ Vertical scroll primary
```
```
/* ✗ */ Horizontal swipe carousel only
```

---

### 25. Tap Delay 🟡 *Medium*

300ms tap delay feels laggy

**Do:** Use touch-action CSS or fastclick
**Don't:** Default mobile tap handling

```
/* ✓ */ touch-action: manipulation
```
```
/* ✗ */ No touch optimization
```

---

### 26. Pull to Refresh ⚪ *Low*

Accidental refresh is frustrating

**Do:** Disable where not needed
**Don't:** Enable by default everywhere

```
/* ✓ */ overscroll-behavior: contain
```
```
/* ✗ */ Default overscroll
```

---

### 27. Haptic Feedback ⚪ *Low*

Tactile feedback improves interaction feel

**Do:** Use for confirmations and important actions
**Don't:** Overuse vibration feedback

```
/* ✓ */ navigator.vibrate(10)
```
```
/* ✗ */ Vibrate on every tap
```

---

## Typography

### 72. Line Height 🟡 *Medium*

Adequate line height improves readability

**Do:** Use 1.5-1.75 for body text
**Don't:** Cramped or excessive line height

```
/* ✓ */ leading-relaxed (1.625)
```
```
/* ✗ */ leading-none (1)
```

---

### 73. Line Length 🟡 *Medium*

Long lines are hard to read

**Do:** Limit to 65-75 characters per line
**Don't:** Full-width text on large screens

```
/* ✓ */ max-w-prose
```
```
/* ✗ */ Full viewport width text
```

---

### 74. Font Size Scale 🟡 *Medium*

Consistent type hierarchy aids scanning

**Do:** Use consistent modular scale
**Don't:** Random font sizes

```
/* ✓ */ Type scale (12 14 16 18 24 32)
```
```
/* ✗ */ Arbitrary sizes
```

---

### 75. Font Loading 🟡 *Medium*

Fonts should load without layout shift

**Do:** Reserve space with fallback font
**Don't:** Layout shift when fonts load

```
/* ✓ */ font-display: swap + similar fallback
```
```
/* ✗ */ No fallback font
```

---

### 76. Contrast Readability 🟠 *High*

Body text needs good contrast

**Do:** Use darker text on light backgrounds
**Don't:** Gray text on gray background

```
/* ✓ */ text-gray-900 on white
```
```
/* ✗ */ text-gray-400 on gray-100
```

---

### 77. Heading Clarity 🟡 *Medium*

Headings should stand out from body

**Do:** Clear size/weight difference
**Don't:** Headings similar to body text

```
/* ✓ */ Bold + larger size
```
```
/* ✗ */ Same size as body
```

---

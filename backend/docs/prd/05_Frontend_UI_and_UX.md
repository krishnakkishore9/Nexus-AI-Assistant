# 05 - Frontend UI & UX Specification

## 🎨 1. Design Language
The app uses a **Modern Glassmorphic Dark Mode** aesthetic, built with Tailwind CSS.

### A. Color Palette
*   **Background**: `slate-950` (#020617)
*   **Cards**: `rgba(255, 255, 255, 0.05)` with `backdrop-blur-xl`.
*   **Accents**: `indigo-500` (#6366f1) for buttons, `cyan-400` for weather, `orange-400` for news.

## 🧱 2. Core Components

### A. Navigation Bar
*   Shows Logo on left.
*   Shows User Profile / Logout on right.
*   Sticky positioning with background blur.

### B. Search Interface (The "Command Center")
*   Center-aligned large input field.
*   Animated "Search" button with a glowing hover effect.
*   Input field should have a "shimmer" effect on focus.

### C. Results Grid
*   **Weather Card**: Displays temperature as a large number, icons for conditions, and Humidity/Wind.
*   **News List**: Scrollable vertical list with thumbnail images, headline titles, and "Source" tags.
*   **Web Results**: Clean list with breadcrumbs and snippets.

## ✨ 3. Animations & Motion

### A. Interaction Feedback
*   **Buttons**: Scale down slightly (0.95) on click.
*   **Input**: Border color transitions smoothly from slate to indigo on focus.

### B. Data Loading
*   **Skeleton Screens**: Show pulse-animated placeholders while data is fetching.
*   **Staggered Entry**: Once data arrives, cards should fade in and slide up sequentially (50ms stagger).

## 📱 4. Responsiveness
*   **Mobile**: Single column layout. Search bar takes full width. Headers slightly smaller.
*   **Tablet**: 2-column grid for news/search results.
*   **Desktop**: Full layout with sidebar options and 3-column feature grid.

---
> [!TIP]
> Use the `Animate.css` library or Tailwind's built-in `transition` and `animate-pulse` utilities to achieve these effects with minimal code.

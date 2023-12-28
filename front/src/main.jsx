import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./index.css";
import ArticleDetail from "./components/ArticleDetail.jsx";
import { ArticleProvider } from "./components/context/ArticleContext.jsx";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <Router>
      <ArticleProvider>
        <Routes>
          <Route path="/*" element={<App />} />
          <Route path="/article/:slug" element={<ArticleDetail />} />
        </Routes>
      </ArticleProvider>
    </Router>
  </React.StrictMode>
);

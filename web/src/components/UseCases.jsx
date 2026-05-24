import { useState, useMemo } from "react";

const GITHUB_BASE =
  "https://github.com/NousResearch/hermes_agent_fullguide/blob/main/docs/use-cases";

const CATEGORIES = [
  {
    id: "daily-life",
    label: "Daily Life",
    icon: "🏠",
    color: "var(--green)",
    tagClass: "tag-green",
    docPath: "daily-life",
    items: [
      { id: "recipe-from-ingredients", icon: "🍳", title: "Recipe from Ingredients", desc: "Generate a recipe from whatever ingredients you have on hand." },
      { id: "weekly-meal-planner", icon: "📅", title: "Weekly Meal Planner", desc: "Build a balanced 7-day meal plan tailored to your dietary goals." },
      { id: "grocery-list-optimizer", icon: "🛒", title: "Grocery List Optimizer", desc: "Turn a meal plan into a consolidated, aisle-sorted grocery list." },
      { id: "nutrition-tracker", icon: "🥗", title: "Nutrition Tracker", desc: "Log meals and get a breakdown of macros and micronutrients." },
      { id: "fitness-workout-planner", icon: "🏋️", title: "Fitness Workout Planner", desc: "Create a weekly workout schedule matched to your fitness level." },
      { id: "sleep-schedule-optimizer", icon: "😴", title: "Sleep Schedule Optimizer", desc: "Suggest a sleep routine based on your wake time and lifestyle." },
      { id: "morning-routine-planner", icon: "☀️", title: "Morning Routine Planner", desc: "Design a timed morning routine that fits your schedule." },
      { id: "home-cleaning-schedule", icon: "🧹", title: "Home Cleaning Schedule", desc: "Generate a recurring cleaning rota for every room in your home." },
      { id: "home-repair-troubleshooter", icon: "🔨", title: "Home Repair Troubleshooter", desc: "Diagnose common household problems and suggest DIY fixes." },
      { id: "plant-care-assistant", icon: "🪴", title: "Plant Care Assistant", desc: "Provide watering, light, and fertilizer advice for your plants." },
      { id: "pet-care-advisor", icon: "🐾", title: "Pet Care Advisor", desc: "Answer breed-specific diet, exercise, and health questions." },
      { id: "outfit-suggester", icon: "👗", title: "Outfit Suggester", desc: "Recommend outfits from your wardrobe for any occasion or weather." },
      { id: "travel-packing-list", icon: "🧳", title: "Travel Packing List", desc: "Build a complete packing checklist from trip type and duration." },
      { id: "vacation-itinerary-planner", icon: "✈️", title: "Vacation Itinerary Planner", desc: "Draft a day-by-day travel itinerary with activities and logistics." },
      { id: "restaurant-recommender", icon: "🍽️", title: "Restaurant Recommender", desc: "Suggest restaurants by cuisine, budget, and location context." },
      { id: "book-movie-recommender", icon: "📖", title: "Book & Movie Recommender", desc: "Recommend books or films based on your taste and mood." },
      { id: "gift-idea-generator", icon: "🎁", title: "Gift Idea Generator", desc: "Produce personalized gift ideas for any person, occasion, and budget." },
      { id: "party-planner", icon: "🎉", title: "Party Planner", desc: "Plan a party end-to-end: theme, food, activities, and timeline." },
      { id: "personal-budget-advisor", icon: "💰", title: "Personal Budget Advisor", desc: "Review monthly spending and suggest where to cut back." },
      { id: "habit-tracker-coach", icon: "✅", title: "Habit Tracker Coach", desc: "Set habit goals, track streaks, and get motivational nudges." },
    ],
  },
  {
    id: "work-productivity",
    label: "Work & Productivity",
    icon: "💼",
    color: "var(--blue)",
    tagClass: "tag-blue",
    docPath: "work-productivity",
    items: [
      { id: "email-drafter", icon: "📧", title: "Email Drafter", desc: "Draft professional emails from a bullet-point brief." },
      { id: "meeting-agenda-generator", icon: "📋", title: "Meeting Agenda Generator", desc: "Create a structured agenda from a meeting title and goals." },
      { id: "meeting-notes-summarizer", icon: "📝", title: "Meeting Notes Summarizer", desc: "Condense raw meeting notes into decisions, actions, and owners." },
      { id: "report-writer", icon: "📄", title: "Report Writer", desc: "Turn data and bullet points into a polished written report." },
      { id: "presentation-outline", icon: "🖥️", title: "Presentation Outline", desc: "Generate a slide-by-slide outline for any topic and audience." },
      { id: "task-prioritizer", icon: "🎯", title: "Task Prioritizer", desc: "Rank a to-do list by urgency and importance (Eisenhower matrix)." },
      { id: "project-timeline-estimator", icon: "📊", title: "Project Timeline Estimator", desc: "Estimate task durations and build a project timeline with milestones." },
      { id: "cover-letter-writer", icon: "✉️", title: "Cover Letter Writer", desc: "Write a tailored cover letter from a resume and job description." },
      { id: "resume-reviewer", icon: "📃", title: "Resume Reviewer", desc: "Give line-by-line feedback on a resume for a target role." },
      { id: "interview-prep", icon: "🎤", title: "Interview Prep", desc: "Generate role-specific interview questions and model answers." },
      { id: "performance-review-writer", icon: "⭐", title: "Performance Review Writer", desc: "Draft a self-review or manager review from accomplishment notes." },
      { id: "onboarding-doc-generator", icon: "🗂️", title: "Onboarding Doc Generator", desc: "Create a new-hire onboarding guide from a role description." },
      { id: "sop-writer", icon: "📑", title: "SOP Writer", desc: "Convert a rough process description into a formal SOP document." },
      { id: "retrospective-facilitator", icon: "🔄", title: "Retrospective Facilitator", desc: "Generate structured retro prompts and summarize team feedback." },
      { id: "okr-goal-setter", icon: "🏆", title: "OKR Goal Setter", desc: "Draft OKRs with measurable key results from a strategic objective." },
      { id: "tone-checker", icon: "🗣️", title: "Tone Checker", desc: "Analyze text tone and suggest rewrites for a target voice." },
      { id: "contract-summarizer", icon: "📜", title: "Contract Summarizer", desc: "Extract key clauses, obligations, and red flags from a contract." },
      { id: "invoice-generator", icon: "🧾", title: "Invoice Generator", desc: "Generate a formatted invoice from project details and line items." },
      { id: "expense-categorizer", icon: "💳", title: "Expense Categorizer", desc: "Parse a bank statement and assign each transaction to a category." },
      { id: "business-idea-validator", icon: "💡", title: "Business Idea Validator", desc: "Stress-test a business idea with market, risk, and viability analysis." },
    ],
  },
  {
    id: "technical",
    label: "Technical & Dev",
    icon: "⚙️",
    color: "var(--purple)",
    tagClass: "tag-purple",
    docPath: "technical",
    items: [
      { id: "code-reviewer", icon: "🔍", title: "Code Reviewer", desc: "Review a code diff for bugs, style issues, and best practices." },
      { id: "bug-explainer", icon: "🐛", title: "Bug Explainer", desc: "Explain why a piece of code is broken and how to fix it." },
      { id: "unit-test-generator", icon: "🧪", title: "Unit Test Generator", desc: "Generate unit tests with edge cases for a given function." },
      { id: "docstring-writer", icon: "📝", title: "Docstring Writer", desc: "Write docstrings or JSDoc comments for undocumented code." },
      { id: "code-refactorer", icon: "♻️", title: "Code Refactorer", desc: "Refactor code for readability, performance, or idiomatic style." },
      { id: "sql-query-builder", icon: "🗄️", title: "SQL Query Builder", desc: "Convert a plain-English question into a SQL query with explanation." },
      { id: "regex-generator", icon: "🔤", title: "Regex Generator", desc: "Build and explain a regular expression from a description." },
      { id: "shell-script-generator", icon: "🖥️", title: "Shell Script Generator", desc: "Write a bash/zsh script from a step-by-step description." },
      { id: "dockerfile-generator", icon: "🐳", title: "Dockerfile Generator", desc: "Create an optimized Dockerfile for a given language and framework." },
      { id: "api-doc-generator", icon: "📡", title: "API Doc Generator", desc: "Generate OpenAPI / REST documentation from code or schema." },
      { id: "git-commit-message-writer", icon: "💾", title: "Git Commit Message Writer", desc: "Draft a Conventional Commits message from a git diff." },
      { id: "code-complexity-explainer", icon: "📈", title: "Code Complexity Explainer", desc: "Explain Big-O complexity and bottlenecks in a function." },
      { id: "security-vulnerability-scanner", icon: "🔒", title: "Security Vulnerability Scanner", desc: "Identify common security issues (OWASP top 10) in source code." },
      { id: "database-schema-designer", icon: "🗃️", title: "Database Schema Designer", desc: "Design a normalized database schema from a requirements description." },
      { id: "algorithm-explainer", icon: "🧮", title: "Algorithm Explainer", desc: "Explain how an algorithm works with step-by-step walkthroughs." },
      { id: "log-analyzer", icon: "📋", title: "Log Analyzer", desc: "Parse log files and surface errors, warnings, and patterns." },
      { id: "error-message-decoder", icon: "❌", title: "Error Message Decoder", desc: "Decode a cryptic error message into plain English with next steps." },
      { id: "dependency-analyzer", icon: "🔗", title: "Dependency Analyzer", desc: "Audit dependencies for outdated packages and known vulnerabilities." },
      { id: "cicd-pipeline-advisor", icon: "🚀", title: "CI/CD Pipeline Advisor", desc: "Suggest CI/CD pipeline stages and config for a given tech stack." },
      { id: "architecture-advisor", icon: "🏗️", title: "Architecture Advisor", desc: "Recommend a system architecture given project constraints and scale." },
    ],
  },
  {
    id: "education",
    label: "Education",
    icon: "🎓",
    color: "var(--yellow)",
    tagClass: "tag-yellow",
    docPath: "education",
    items: [
      { id: "flashcard-generator", icon: "🃏", title: "Flashcard Generator", desc: "Create Anki-style flashcards from any text or topic." },
      { id: "quiz-creator", icon: "❓", title: "Quiz Creator", desc: "Generate multiple-choice or open-ended quizzes with answer keys." },
      { id: "study-plan-maker", icon: "📅", title: "Study Plan Maker", desc: "Build a study schedule for an exam from today until the test date." },
      { id: "essay-feedback", icon: "✍️", title: "Essay Feedback", desc: "Give structured feedback on an essay: thesis, structure, and style." },
      { id: "math-problem-solver", icon: "➗", title: "Math Problem Solver", desc: "Solve math problems step-by-step with full working shown." },
      { id: "language-tutor", icon: "🗣️", title: "Language Tutor", desc: "Practice conversation, grammar, and vocabulary in any language." },
      { id: "history-explainer", icon: "🏛️", title: "History Explainer", desc: "Explain historical events with context, causes, and consequences." },
      { id: "science-simplifier", icon: "🔬", title: "Science Simplifier", desc: "Break down complex scientific concepts for any audience level." },
      { id: "vocabulary-builder", icon: "📚", title: "Vocabulary Builder", desc: "Teach new words with definitions, etymology, and example sentences." },
      { id: "reading-comprehension", icon: "👁️", title: "Reading Comprehension", desc: "Generate comprehension questions and summaries for a text passage." },
      { id: "debate-argument-generator", icon: "⚖️", title: "Debate Argument Generator", desc: "Build arguments for and against any debate topic." },
      { id: "research-paper-summarizer", icon: "🔭", title: "Research Paper Summarizer", desc: "Summarize an academic paper into abstract, methods, and findings." },
      { id: "citation-formatter", icon: "📌", title: "Citation Formatter", desc: "Convert a source into APA, MLA, Chicago, or Harvard format." },
      { id: "concept-map-creator", icon: "🗺️", title: "Concept Map Creator", desc: "Generate a textual concept map linking ideas in a topic." },
      { id: "exam-strategy-advisor", icon: "🏅", title: "Exam Strategy Advisor", desc: "Advise on exam technique, time management, and revision tactics." },
    ],
  },
  {
    id: "health-wellness",
    label: "Health & Wellness",
    icon: "❤️",
    color: "var(--red)",
    tagClass: "tag-green",
    docPath: "health-wellness",
    items: [
      { id: "symptom-diary-analyzer", icon: "📓", title: "Symptom Diary Analyzer", desc: "Spot patterns in a symptom log and produce a summary for a doctor." },
      { id: "medication-interaction-checker", icon: "💊", title: "Medication Interaction Checker", desc: "Flag potential interactions between a list of medications." },
      { id: "mental-health-journaling", icon: "🧠", title: "Mental Health Journaling", desc: "Guide a CBT-style journaling session and reflect key insights back." },
      { id: "mindfulness-meditation-guide", icon: "🧘", title: "Mindfulness Meditation Guide", desc: "Lead a timed guided meditation script for focus or sleep." },
      { id: "hydration-reminder", icon: "💧", title: "Hydration Reminder", desc: "Calculate daily water targets and create a reminder schedule." },
      { id: "ergonomics-advisor", icon: "🪑", title: "Ergonomics Advisor", desc: "Evaluate a workspace setup and suggest ergonomic improvements." },
      { id: "first-aid-guide", icon: "🩹", title: "First Aid Guide", desc: "Provide step-by-step first aid instructions for common situations." },
      { id: "workout-form-explainer", icon: "🏃", title: "Workout Form Explainer", desc: "Describe correct form and common mistakes for any exercise." },
      { id: "nutrition-label-decoder", icon: "🏷️", title: "Nutrition Label Decoder", desc: "Interpret a nutrition label and flag items of concern." },
      { id: "allergy-recipe-adapter", icon: "🥜", title: "Allergy Recipe Adapter", desc: "Rewrite a recipe to remove specified allergens with substitutions." },
    ],
  },
  {
    id: "finance",
    label: "Finance",
    icon: "💹",
    color: "var(--green)",
    tagClass: "tag-green",
    docPath: "finance",
    items: [
      { id: "personal-budget-analyzer", icon: "📊", title: "Personal Budget Analyzer", desc: "Analyze income vs. expenses and produce a spending health score." },
      { id: "investment-explainer", icon: "📈", title: "Investment Explainer", desc: "Explain investment vehicles (stocks, bonds, ETFs) in plain language." },
      { id: "tax-deduction-finder", icon: "🧾", title: "Tax Deduction Finder", desc: "Identify likely deductions from a list of annual expenses." },
      { id: "subscription-audit", icon: "🔁", title: "Subscription Audit", desc: "Review recurring charges and flag unused or duplicated subscriptions." },
      { id: "salary-negotiation-coach", icon: "🤝", title: "Salary Negotiation Coach", desc: "Prepare scripts and counter-offer strategies for salary talks." },
      { id: "loan-comparison", icon: "🏦", title: "Loan Comparison", desc: "Compare loan offers by total cost, APR, and monthly payment." },
      { id: "credit-card-optimizer", icon: "💳", title: "Credit Card Optimizer", desc: "Suggest which card to use for each spending category to maximize rewards." },
      { id: "retirement-planner", icon: "👴", title: "Retirement Planner", desc: "Project retirement savings based on current contributions and rate." },
      { id: "side-hustle-tracker", icon: "🛠️", title: "Side Hustle Tracker", desc: "Log side income, estimate taxes owed, and track profitability." },
      { id: "emergency-fund-calculator", icon: "🆘", title: "Emergency Fund Calculator", desc: "Calculate target emergency fund size and a month-by-month savings plan." },
    ],
  },
  {
    id: "creative",
    label: "Creative",
    icon: "🎨",
    color: "var(--purple)",
    tagClass: "tag-purple",
    docPath: "creative",
    items: [
      { id: "short-story-generator", icon: "📖", title: "Short Story Generator", desc: "Write a short story from a genre, setting, and character brief." },
      { id: "songwriting-assistant", icon: "🎵", title: "Songwriting Assistant", desc: "Help write lyrics with rhyme, meter, and theme guidance." },
      { id: "poem-generator", icon: "🖊️", title: "Poem Generator", desc: "Generate a poem in any form (haiku, sonnet, free verse) on any topic." },
      { id: "social-media-caption-writer", icon: "📱", title: "Social Media Caption Writer", desc: "Craft platform-optimized captions with hashtags and CTAs." },
      { id: "brand-naming-assistant", icon: "🏷️", title: "Brand Naming Assistant", desc: "Generate and evaluate brand name candidates with rationale." },
    ],
  },
];

function getQuickstart(catDocPath, itemId) {
  return `hermes run ${catDocPath}/${itemId} --model hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF`;
}

function getDemoPrompt(item) {
  return `Use the ${item.title} use case: ${item.desc}`;
}

export default function UseCases() {
  const [activeCat, setActiveCat] = useState(CATEGORIES[0].id);
  const [search, setSearch] = useState("");
  const [selected, setSelected] = useState(null); // { item, cat }

  const category = CATEGORIES.find(c => c.id === activeCat);

  const searchLower = search.trim().toLowerCase();
  const isSearching = searchLower.length > 0;

  const searchResults = useMemo(() => {
    if (!isSearching) return [];
    const results = [];
    for (const cat of CATEGORIES) {
      for (const item of cat.items) {
        if (
          item.title.toLowerCase().includes(searchLower) ||
          item.desc.toLowerCase().includes(searchLower) ||
          cat.label.toLowerCase().includes(searchLower)
        ) {
          results.push({ item, cat });
        }
      }
    }
    return results;
  }, [searchLower, isSearching]);

  const displayItems = isSearching
    ? searchResults
    : category.items.map(item => ({ item, cat: category }));

  function handleTryDemo(item) {
    const prompt = getDemoPrompt(item);
    localStorage.setItem("hermes_demo_prompt", prompt);
    window.location.hash = "#demo";
    setSelected(null);
  }

  return (
    <section id="use-cases" className="section" style={{ borderTop: "1px solid var(--border)" }}>
      <div className="container">
        {/* Header */}
        <div style={{ marginBottom: 40 }}>
          <div className="section-label">100 use cases</div>
          <h2 className="section-title">From daily life to dev tools</h2>
          <p className="section-sub">Every use case is a runnable offline script. No API key. No cloud.</p>
        </div>

        {/* Search */}
        <div style={{ marginBottom: 28, position: "relative" }}>
          <span style={{
            position: "absolute", left: 14, top: "50%", transform: "translateY(-50%)",
            fontSize: 16, color: "var(--text3)", pointerEvents: "none",
          }}>🔍</span>
          <input
            value={search}
            onChange={e => setSearch(e.target.value)}
            placeholder="Search all 100 use cases…"
            style={{
              width: "100%", padding: "11px 16px 11px 42px",
              background: "var(--bg2)", border: "1px solid var(--border)",
              borderRadius: "var(--radius-sm)", color: "var(--text)",
              fontSize: 14, outline: "none", transition: "border-color 0.15s",
            }}
            onFocus={e => e.target.style.borderColor = "var(--blue)"}
            onBlur={e => e.target.style.borderColor = "var(--border)"}
          />
          {search && (
            <button onClick={() => setSearch("")} style={{
              position: "absolute", right: 12, top: "50%", transform: "translateY(-50%)",
              background: "none", border: "none", color: "var(--text3)", cursor: "pointer",
              fontSize: 16, lineHeight: 1,
            }}>✕</button>
          )}
        </div>

        {/* Category Tabs — hidden when searching */}
        {!isSearching && (
          <div style={{
            display: "flex", gap: 6, marginBottom: 28, flexWrap: "wrap",
          }}>
            {CATEGORIES.map(cat => (
              <button
                key={cat.id}
                onClick={() => { setActiveCat(cat.id); setSelected(null); }}
                style={{
                  padding: "7px 14px", borderRadius: "var(--radius-sm)",
                  border: "1px solid",
                  borderColor: activeCat === cat.id ? "var(--blue)" : "var(--border)",
                  background: activeCat === cat.id ? "var(--blue-glow)" : "transparent",
                  color: activeCat === cat.id ? "var(--text)" : "var(--text2)",
                  fontSize: 13, fontWeight: 600, cursor: "pointer",
                  display: "flex", alignItems: "center", gap: 6,
                  transition: "all 0.15s",
                }}
              >
                <span>{cat.icon}</span>
                <span>{cat.label}</span>
                <span style={{
                  background: activeCat === cat.id ? "var(--blue)" : "var(--bg3)",
                  color: activeCat === cat.id ? "#fff" : "var(--text3)",
                  borderRadius: 999, padding: "1px 7px", fontSize: 11, fontWeight: 700,
                }}>{cat.items.length}</span>
              </button>
            ))}
          </div>
        )}

        {/* Search result label */}
        {isSearching && (
          <div style={{ marginBottom: 16, fontSize: 13, color: "var(--text3)" }}>
            {searchResults.length} result{searchResults.length !== 1 ? "s" : ""} for &ldquo;{search}&rdquo;
          </div>
        )}

        {/* Main layout: grid + detail panel */}
        <div style={{
          display: "grid",
          gridTemplateColumns: selected ? "1fr 380px" : "1fr",
          gap: 20,
          alignItems: "start",
        }}>
          {/* Cards grid */}
          <div>
            {displayItems.length === 0 ? (
              <div style={{
                padding: "48px 0", textAlign: "center",
                color: "var(--text3)", fontSize: 15,
              }}>
                No use cases match your search.
              </div>
            ) : (
              <div style={{
                display: "grid",
                gridTemplateColumns: "repeat(auto-fill, minmax(220px, 1fr))",
                gap: 12,
              }}>
                {displayItems.map(({ item, cat }) => {
                  const isActive = selected && selected.item.id === item.id;
                  return (
                    <button
                      key={`${cat.id}-${item.id}`}
                      onClick={() => setSelected(isActive ? null : { item, cat })}
                      style={{
                        textAlign: "left", cursor: "pointer",
                        background: isActive ? "var(--blue-glow)" : "var(--bg2)",
                        border: "1px solid",
                        borderColor: isActive ? "var(--blue)" : "var(--border)",
                        borderRadius: "var(--radius)", padding: "16px",
                        display: "flex", flexDirection: "column", gap: 8,
                        transition: "all 0.15s",
                      }}
                      onMouseEnter={e => { if (!isActive) e.currentTarget.style.borderColor = "var(--border2)"; }}
                      onMouseLeave={e => { if (!isActive) e.currentTarget.style.borderColor = "var(--border)"; }}
                    >
                      <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
                        <span style={{ fontSize: 22 }}>{item.icon}</span>
                        {isSearching && (
                          <span className={`tag ${cat.tagClass}`} style={{ fontSize: 10 }}>{cat.label}</span>
                        )}
                      </div>
                      <div style={{ fontWeight: 700, fontSize: 13, color: "var(--text)", lineHeight: 1.35 }}>
                        {item.title}
                      </div>
                      <div style={{ fontSize: 12, color: "var(--text3)", lineHeight: 1.55 }}>
                        {item.desc}
                      </div>
                    </button>
                  );
                })}
              </div>
            )}
          </div>

          {/* Detail panel */}
          {selected && (
            <div className="card" style={{
              display: "flex", flexDirection: "column", gap: 20,
              position: "sticky", top: 24,
            }}>
              {/* Close */}
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
                <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
                  <span style={{ fontSize: 28 }}>{selected.item.icon}</span>
                  <h3 style={{ fontSize: 17, fontWeight: 700, lineHeight: 1.3 }}>{selected.item.title}</h3>
                </div>
                <button
                  onClick={() => setSelected(null)}
                  style={{
                    background: "none", border: "none", color: "var(--text3)",
                    cursor: "pointer", fontSize: 18, lineHeight: 1, flexShrink: 0,
                  }}
                >✕</button>
              </div>

              {/* Category badge */}
              <div>
                <span className={`tag ${selected.cat.tagClass}`}>
                  {selected.cat.icon} {selected.cat.label}
                </span>
              </div>

              {/* Description */}
              <p style={{ fontSize: 14, color: "var(--text2)", lineHeight: 1.65 }}>
                {selected.item.desc}
              </p>

              {/* Quickstart */}
              <div>
                <div style={{ fontSize: 11, fontWeight: 700, color: "var(--text3)", marginBottom: 8, letterSpacing: "0.06em" }}>
                  QUICKSTART
                </div>
                <div className="code-block" style={{ fontSize: 12 }}>
                  <span className="cmd">$</span>{" "}
                  {getQuickstart(selected.cat.docPath, selected.item.id)}
                </div>
              </div>

              {/* Actions */}
              <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
                <a
                  href={`${GITHUB_BASE}/${selected.cat.docPath}/${selected.item.id}.md`}
                  target="_blank"
                  rel="noreferrer"
                  className="btn btn-secondary"
                  style={{ justifyContent: "center", fontSize: 13 }}
                >
                  📄 View Doc on GitHub
                </a>
                <button
                  className="btn btn-primary"
                  style={{ justifyContent: "center", fontSize: 13 }}
                  onClick={() => handleTryDemo(selected.item)}
                >
                  ▶ Try in Demo
                </button>
              </div>
            </div>
          )}
        </div>
      </div>
    </section>
  );
}

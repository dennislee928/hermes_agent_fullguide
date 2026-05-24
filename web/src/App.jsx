import Nav from "./components/Nav.jsx";
import Hero from "./components/Hero.jsx";
import Features from "./components/Features.jsx";
import SetupGuide from "./components/SetupGuide.jsx";
import LiveDemo from "./components/LiveDemo.jsx";
import UseCases from "./components/UseCases.jsx";
import Downloads from "./components/Downloads.jsx";
import Footer from "./components/Footer.jsx";

export default function App() {
  return (
    <>
      <Nav />
      <main>
        <Hero />
        <Features />
        <SetupGuide />
        <LiveDemo />
        <UseCases />
        <Downloads />
      </main>
      <Footer />
    </>
  );
}

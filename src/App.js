import React, { useState, useEffect } from 'react';
import './App.css';
import { motion } from 'framer-motion';
import { Link, animateScroll as scroll } from 'react-scroll';
import { FaBars } from 'react-icons/fa';
import { scroller } from 'react-scroll';


import About from './components/About.jsx';
import Skills from './components/Skills.jsx';
import Portfolio from './components/Portfolio.jsx';
import Contact from './components/Contact.jsx';

function App() {
  const [showButton, setShowButton] = useState(true);
  const [menuOpen, setMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      const scrollableContainer = document.getElementById('app-container');
      if (scrollableContainer) {
        setShowButton(scrollableContainer.scrollTop > 300);
      } else {
        setShowButton(window.scrollY > 300);
      }
    };

    const scrollableContainer = document.getElementById('app-container');
    if (scrollableContainer) {
      scrollableContainer.addEventListener('scroll', handleScroll);
    } else {
      window.addEventListener('scroll', handleScroll);
    }

    return () => {
      if (scrollableContainer) {
        scrollableContainer.removeEventListener('scroll', handleScroll);
      } else {
        window.removeEventListener('scroll', handleScroll);
      }
    };
  }, []);

  const scrollToHome = () => {
  scroller.scrollTo('home', {
    smooth: true,
    duration: 800,
    offset: -60,
  });
};


  return (
    <div className="container" id="app-container">
      <header className="main-header">
        <div className="header-logo">İrem İclal Karapınar</div>
        <div className="menu-toggle" onClick={() => setMenuOpen(!menuOpen)}>
          <FaBars />
        </div>
        <nav className={`main-nav-menu ${menuOpen ? 'open' : ''}`}>
          <Link to="home" smooth={true} duration={200} offset={-60} onClick={() => { setTimeout(() => {setMenuOpen(false); }, 300); }} className="nav-link">Ana Sayfa</Link>
          <Link to="about-section" smooth={true} duration={200} offset={-60} onClick={() => { setTimeout(() => {setMenuOpen(false); }, 300); }} className="nav-link">Ben Kimim?</Link>
          <Link to="skills-section" smooth={true} duration={200} offset={-60} onClick={() => { setTimeout(() => {setMenuOpen(false); }, 300); }} className="nav-link">Neler Yapabilirim?</Link>
          <Link to="portfolio-section" smooth={true} duration={200} offset={-60} onClick={() => { setTimeout(() => {setMenuOpen(false); }, 300); }} className="nav-link">Portfolyo</Link>
          <Link to="contact-section" smooth={true} duration={200} offset={-60} onClick={() => { setTimeout(() => {setMenuOpen(false); }, 300); }} className="nav-link">İletişim</Link>
        </nav>
      </header>

      <main className="hero-section" id="home">
        <div className="hero-image">
          <img src="/profile-image.jpg" alt="İrem İclal Karapınar" />
        </div>

        <motion.div
          className="hero-text"
          initial={{ opacity: 0, y: 50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1.2, ease: "easeOut" }}
        >
          <div className="intro-line">Merhaba, ben</div>
          <div className="name-line">İrem İclal Karapınar.</div>
        </motion.div>

        <div className="contact-info">
          <a href="https://github.com/icalliope" target="_blank" rel="noopener noreferrer">
            <img src="/img/icons8-github-logo-100.png" alt="GitHub" className="icon" />
          </a>
          <a href="https://www.linkedin.com/in/irem-iclal-karapinar" target="_blank" rel="noopener noreferrer">
            <img src="/img/icons8-linkedin-100.png" alt="LinkedIn" className="icon" />
          </a>
          <a href="https://www.instagram.com/kullaniciadiniz" target="_blank" rel="noopener noreferrer">
            <img src="/img/icons8-instagram-logo-100.png" alt="Instagram" className="icon" />
          </a>
          <a href="https://www.x.com" target="_blank" rel="noopener noreferrer">
            <img src="/img/icons8-x-100.png" alt="X" className="icon" />
          </a>
          <a href="https://www.facebook.com" target="_blank" rel="noopener noreferrer">
            <img src="/img/icons8-facebook-logo-100.png" alt="Facebook" className="icon" />
          </a>
        </div>
      </main>

      <section id="about-section"><About /></section>
      <section id="skills-section"><Skills /></section>
      <section id="portfolio-section"><Portfolio /></section>
      <section id="contact-section"><Contact /></section>

      {showButton && (
        <button
          onClick={scrollToHome}
          className="scroll-to-top-button"
          aria-label="Ana Sayfaya Git"
        >
          <img src="/img/icons8-up-96.png" alt="Ana Sayfaya Git" className="button-icon" />
        </button>
      )}
    </div>
  );
}

export default App;

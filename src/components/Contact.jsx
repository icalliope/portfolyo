import React from 'react';
import './Contact.css';

const Contact = () => {
  return (
    <section className="contact-section">
      <div className="contact-container">

        <form className="contact-form">
          <h2>İletişim</h2>
          <input type="text" placeholder="Adınız" />
          <input type="email" placeholder="E-posta" />
          <textarea placeholder="Mesajınız" />
          <button type="submit">Gönder</button>
        </form>

        <div className="contact-info-card">
          <h3>İletişim Bilgilerim</h3>
          <p>
            <img src="/img/icons8-phone-24.png" alt="Telefon" className="icon" />
            +90 542 618 13 80
          </p>
          <p>
            <img src="/img/icons8-mail-24.png" alt="E-posta" className="icon" />
            iclal.irem2004@gmail.com
          </p>


          <div className="social-icons">
            <a href="https://github.com/icalliope" target="_blank" rel="noopener noreferrer">
              <img src="/img/icons8-github-logo-100.png" alt="GitHub" />
            </a>
            <a href="https://www.linkedin.com/in/irem-iclal-karapinar" target="_blank" rel="noopener noreferrer">
              <img src="/img/icons8-linkedin-100.png" alt="LinkedIn" />
            </a>
            <a href="https://www.instagram.com/kullaniciadiniz" target="_blank" rel="noopener noreferrer">
              <img src="/img/icons8-instagram-logo-100.png" alt="Instagram" />
            </a>
            <a href="https://x.com/kullaniciadiniz" target="_blank" rel="noopener noreferrer">
              <img src="/img/icons8-x-100.png" alt="X" />
            </a>
            <a href="https://www.facebook.com" target="_blank" rel="noopener noreferrer">
            <img src="/img/icons8-facebook-logo-100.png" alt="Facebook"  />
          </a>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Contact;

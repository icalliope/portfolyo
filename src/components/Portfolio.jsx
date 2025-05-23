import React from 'react';
import './Portfolio.css';

const Portfolio = () => {
  return (
    <section className="portfolio-section">
      <div className="timeline">
        <div className="line"></div>
        <div className="timeline-card left">
          <h3>Beslenme ve Egzersiz Takip Uygulaması</h3>
          <p>Bu proje, Python programlama dili ve PyQt5 kütüphanesi kullanılarak geliştirilmiş modern bir masaüstü uygulamasıdır. Arayüz tasarımı QSS (Qt Style Sheets) ile özelleştirilmiş olup, kullanıcı dostu bir deneyim sunar. Uygulama, özellikle diyetisyenler veya spor koçları eşliğinde çalışan bireylerin beslenme ve egzersiz takibini daha düzenli ve pratik bir şekilde yapabilmelerini amaçlamaktadır.</p>
        </div>
        <div className="timeline-card right">
          <h3>Notepad</h3>
          <p>Bu masaüstü not uygulaması, kullanıcıların notlarını klasörler halinde düzenlemesine olanak tanır. Python ile geliştirilen projede PyQt5 arayüz kütüphanesi kullanılmış olup, veriler SQLite veritabanında saklanır. Kullanıcılar klasör oluşturabilir, her klasöre not ekleyebilir, bu notları görüntüleyip düzenleyebilir. Notlar tarih bilgisiyle birlikte kaydedilir ve uygulama tamamen çevrimdışı çalışır. Basit ve işlevsel yapısıyla öğrencilerden profesyonellere kadar herkes için ideal bir not yönetim aracıdır.</p>
        </div>
        <div className="timeline-card left">
          <h3>Soru Bankası</h3>
          <p>Bu proje, PyQt5 kullanılarak geliştirilen bir "Soru Bankası" uygulamasıdır. Kullanıcılar sisteme kayıt olup giriş yapabilir, ders seçerek her derse özel çoktan seçmeli sorular ekleyebilir ve doğru cevapları görüntüleyebilir. Uygulama, kullanıcıların kendi sorularını oluşturmasını ve saklamasını sağlayarak kişisel bir soru arşivi oluşturmalarına olanak tanır.</p>
        </div>
        <div className="timeline-card right">
          <h3>Web Sitesi</h3>
          <p>Bu web sitesi, kişisel portfolyomu modern ve interaktif bir tasarımla sunmak amacıyla geliştirilmiştir. Ana sayfada ismim ve sosyal medya bağlantılarım yer alırken, yazı animasyonlarıyla dikkat çekici bir karşılama sağlanır. "Ben Kimim?" bölümünde kendimi tanıttığım kısa bir yazı bulunur ve her bölüm yumuşak geçişlerle birbirine bağlanır. "Neler Yapabilirim?" kısmında becerilerim kart yapısıyla görselleştirilmiş ve hover animasyonlarıyla etkileşim artırılmıştır. Portfolyo bölümünde projelerime dair kısa bilgiler sunulur. İletişim kısmında, kullanıcıların doğrudan bana ulaşabileceği bir mail formu ve iletişim bilgilerim yer almaktadır.</p>
        </div>
      </div>
    </section>
  );
};

export default Portfolio;

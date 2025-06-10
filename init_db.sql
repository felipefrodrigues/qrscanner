CREATE DATABASE IF NOT EXISTS qr_code_db;
USE qr_code_db;

CREATE TABLE IF NOT EXISTS qr_codes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    redirect_url VARCHAR(255),
    id_cliente VARCHAR(100),
    image_url VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS leads (
    id INT AUTO_INCREMENT PRIMARY KEY,
    qr_code_id INT,
    nome_completo VARCHAR(255),
    telefone VARCHAR(50),
    geolocalizacao VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

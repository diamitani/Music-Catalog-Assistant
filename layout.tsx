import React from 'react';
import './layout.css';

const Layout: React.FC<{ children: React.ReactNode }> = ({ children }) => {
    return (
        <div className="layout">
            <header className="header">
                <h1>Music Catalogue Assistant</h1>
            </header>
            <main className="content">{children}</main>
        </div>
    );
};

export default Layout;

import React, { ReactNode } from 'react';
import './AppWrappers.css';

interface AppWrappersProps {
    children: ReactNode;
}

const AppWrappers: React.FC<AppWrappersProps> = ({ children }) => {
    return (
        <div className="app-wrapper">
            {children}
        </div>
    );
};

export default AppWrappers;

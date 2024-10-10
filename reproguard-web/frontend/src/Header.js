import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
    return (
        <header>
            <nav>
                <Link to="/">Home</Link>
                <Link to="/resources">Resources</Link>
                <Link to="/diagnostic-tool">Diagnostic Tool</Link>
                <Link to="/forum">Forum</Link>
            </nav>
        </header>
    );
};

export default Header;
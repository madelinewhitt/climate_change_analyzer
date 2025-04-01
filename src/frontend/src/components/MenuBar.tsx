import { Link } from "react-router-dom";

const MenuBar: React.FC = () => {
  return (
    <nav className="menu-bar">
      <div className="logo-container">
        <Link to="/" className="logo">PyDisasters</Link>
      </div>
      <ul className="menu-items">
        <li className="submenu">
          <Link to="/About">Graphs</Link>
          <ul className="submenu-items">
            <li><Link to="/Graph1">Frequencies</Link></li>
            <li><Link to="/Graph2">Timeline</Link></li>
            <li><Link to="/Graph3">Quantity</Link></li>
          </ul>
        </li>
      </ul>
    </nav>
  );
};

export default MenuBar;


import { Link } from "react-router-dom";

const MenuBar: React.FC = () => {
  return (
    <nav className="bg-green-600 p-4 fixed top-0 left-0 w-full z-50">
      <div className="flex items-center justify-between">
        <div className="logo-container">
          <Link to="/" className="text-white text-2xl font-bold">PyDisasters</Link>
        </div>
        <div className="flex space-x-6">
          <Link
            to="/graph1"
            className="bg-green-700 text-white px-4 py-2 rounded hover:bg-green-800 focus:outline-none focus:ring-2 focus:ring-green-400"
          >
            Interactive Maps
          </Link>
          <Link
            to="/Comparison"
            className="bg-green-700 text-white px-4 py-2 rounded hover:bg-green-800 focus:outline-none focus:ring-2 focus:ring-green-400"
          >
            Predicted Data
          </Link>
          <Link
            to="/Clustering"
            className="bg-green-700 text-white px-4 py-2 rounded hover:bg-green-800 focus:outline-none focus:ring-2 focus:ring-green-400"
          >
            Clustering
          </Link>
          <Link
            to="/Anomalies"
            className="bg-green-700 text-white px-4 py-2 rounded hover:bg-green-800 focus:outline-none focus:ring-2 focus:ring-green-400"
          >
            Anomalies
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default MenuBar;

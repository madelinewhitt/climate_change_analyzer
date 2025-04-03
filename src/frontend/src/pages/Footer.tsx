import { FaGithub } from 'react-icons/fa';  // Import GitHub icon from react-icons

const Footer: React.FC = () => {
    return (
        <footer className="bg-green-600 p-4 text-white text-center fixed bottom-0 left-0 w-full">
            <div className="flex justify-center items-center space-x-2">
                <p>Check out the project on</p>
                <a
                    href="https://github.com/bobromero/climate_change_analyzer/tree/main"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-white hover:text-gray-200"
                >
                    <FaGithub size={30} />
                </a>
            </div>
        </footer>
    );
};

export default Footer;

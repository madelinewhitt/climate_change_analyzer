import React, { useState } from 'react';

const Anomalies: React.FC = () => {
    // Set initial year (1900 by default)
    const [year, setYear] = useState(1900);

    // Function to handle slider change
    const handleYearChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setYear(parseInt(event.target.value, 10));
    };

    // Define the image paths for anomalies and multi-anomalies
    const imagePathAnomalies = `/outputs/anomalies/deaths_${year}.png`;
    const imagePathMultiAnomalies = `/outputs/multianomalies/deaths_${year}.png`;

    // Image path for the key
    const keyImagePath = "/outputs/algorithms/key.png";

    return (
        <div className="Anomalies pt-24">
            <div className="flex flex-col items-center justify-center space-y-6 p-6">
                <h1 className="text-4xl font-semibold">Compare Anomaly Maps</h1>
                <h4 className="text-lg text-center text-gray-700">
                    Use the slider below to compare anomaly maps for a selected year between two algorithms (anomalies vs multi-anomalies).
                </h4>

                <div className="mb-6 w-full max-w-4xl text-center">
                    <img
                        src={keyImagePath}
                        alt="Disaster Types Key"
                        className="w-1/8 mx-auto rounded-lg shadow-xl"
                    />
                </div>

                {/* Two images side by side for the comparison */}
                <div className="flex space-x-6 mb-6 w-full max-w-4xl">
                    {/* First image (Anomalies map) */}
                    <div className="w-1/2">
                        <img
                            src={imagePathAnomalies}
                            alt={`Anomalies Map for ${year}`}
                            className="w-full h-auto rounded-lg shadow-xl"
                        />
                    </div>
                    {/* Second image (Multi-anomalies map) */}
                    <div className="w-1/2">
                        <img
                            src={imagePathMultiAnomalies}
                            alt={`Multi-anomalies Map for ${year}`}
                            className="w-full h-auto rounded-lg shadow-xl"
                        />
                    </div>
                </div>

                {/* Slider control */}
                <div className="mt-6 w-full max-w-2xl">
                    <label htmlFor="slider" className="text-lg text-gray-600">Year: {year}</label>
                    <input
                        id="slider"
                        type="range"
                        min="1900"
                        max="2034"
                        value={year}
                        onChange={handleYearChange}
                        className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer hover:bg-gray-300 focus:ring-2 focus:ring-blue-500"
                    />
                </div>
            </div>
        </div>
    );
};

export default Anomalies;

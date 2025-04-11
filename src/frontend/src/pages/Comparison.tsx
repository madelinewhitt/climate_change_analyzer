import React, { useState } from 'react';

const Comparison: React.FC = () => {
    const [value, setValue] = useState(2025); // default slider value set to 2025

    const handleSliderChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setValue(parseInt(event.target.value, 10));
    };

    // Image paths for both algorithms
    const imagePathAlgorithm = `/outputs/algorithms/algorithm/deaths_${value}.png`;
    const imagePathMultiAlgorithm = `/outputs/algorithms/multialgorithm/deaths_${value}.png`;
    const multiAlgLineGraph = `/outputs/line_graphs/multialgorithms_deaths_by_disaster.png`;
    const singleAlgLineGraph = `/outputs/line_graphs/algorithm_deaths_by_disaster.png`;

    // Image path for the key
    const keyImagePath = "/outputs/algorithms/key.png";

    return (
        <div className="Graph1 pt-24"> {/* Added pt-24 to provide padding-top */}
            <div className="flex flex-col items-center justify-center space-y-6 p-6">
                <h1 className="text-4xl font-semibold">Interactive Future Maps</h1>
                <h4 className="text-lg text-center text-gray-700">
                    Use the slider to scroll through the years (2025-2034) and visualize the corresponding disaster maps generated using different algorithms.
                </h4>

                <div className="mb-6 w-full max-w-4xl text-center">
                    <img
                        src={keyImagePath}
                        alt="Disaster Types Key"
                        className="w-1/8 mx-auto rounded-lg shadow-xl" 
                    />
                </div>

                {/* Two images side by side */}
                <div className="flex space-x-6 mb-6 w-full max-w-4xl">
                    {/* First image (Algorithm) */}
                    <div className="w-1/2">
                        <img
                            src={imagePathAlgorithm}
                            alt={`Algorithm Disaster Map for ${value}`}
                            className="w-full h-auto rounded-lg shadow-xl"
                        />
                    </div>
                    {/* Second image (Multialgorithm) */}
                    <div className="w-1/2">
                        <img
                            src={imagePathMultiAlgorithm}
                            alt={`Multialgorithm Disaster Map for ${value}`}
                            className="w-full h-auto rounded-lg shadow-xl"
                        />
                    </div>
                </div>

                {/* Slider control */}
                <div className="mt-6 w-full max-w-2xl">
                    <label htmlFor="slider" className="text-lg text-gray-600">Year: {value}</label>
                    <input
                        id="slider"
                        type="range"
                        min="2025"
                        max="2034"
                        value={value}
                        onChange={handleSliderChange}
                        className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer hover:bg-gray-300 focus:ring-2 focus:ring-blue-500"
                    />
                </div>
            </div>

            {/* Section for comparing the line graphs */}
            <div className="flex flex-col items-center justify-center space-y-6 p-6 mt-12">
                <h2 className="text-3xl font-semibold">Comparing Line Graphs</h2>
                <h4 className="text-lg text-center text-gray-700">
                    Below are the total deaths by disaster type shown in line graphs for both algorithms.
                </h4>

                {/* Line graph images side by side */}
                <div className="flex space-x-6 mb-6 w-full max-w-4xl">
                    {/* First image (Algorithm line graph) */}
                    <div className="w-1/2">
                        <img
                            src={singleAlgLineGraph}
                            alt="Line graph of total deaths by disaster (Algorithm)"
                            className="w-full h-auto rounded-lg shadow-xl"
                        />
                    </div>
                    {/* Second image (Multialgorithm line graph) */}
                    <div className="w-1/2">
                        <img
                            src={multiAlgLineGraph}
                            alt="Line graph of total deaths by disaster (Multialgorithm)"
                            className="w-full h-auto rounded-lg shadow-xl"
                        />
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Comparison;

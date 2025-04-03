import React, { useState } from 'react';

const Graph1: React.FC = () => {
    const [value, setValue] = useState(1900); // default slider value
    const [disasterType, setDisasterType] = useState('earthquake'); // default disaster type

    const handleSliderChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setValue(parseInt(event.target.value, 10));
    };

    const handleDisasterTypeChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
        setDisasterType(event.target.value);
    };

    const imagePath = `/outputs/${disasterType}_maps/${disasterType}s_${value}.png`;

    return (
        <div className="Graph1 pt-24"> {/* Added pt-24 to provide padding-top */}
            <div className="flex flex-col items-center justify-center space-y-6 p-6">
                <h1 className="text-4xl font-semibold">Interactive Maps</h1>
                <h4 className="text-lg text-center text-gray-700">
                    This interactive map allows you to explore disaster data over time. Use the slider to scroll through the years and visualize how the frequency of each disaster type changes over time. As you move through the years, the map will dynamically update to show the corresponding disaster locations, offering a clear view of disaster trends over time.
                </h4>

                {/* Disaster type image */}
                <div className="mb-6 w-full max-w-4xl">
                    <img
                        src={imagePath}
                        alt={`${disasterType}s in ${value}`}
                        className="w-full h-auto rounded-lg shadow-xl"
                    />
                </div>

                {/* Slider control */}
                <div className="mt-6 w-full max-w-2xl">
                    <label htmlFor="slider" className="text-lg text-gray-600">Year: {value}</label>
                    <input
                        id="slider"
                        type="range"
                        min="1900"
                        max="2025"
                        value={value}
                        onChange={handleSliderChange}
                        className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer hover:bg-gray-300 focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                {/* Dropdown to select disaster type */}
                <div className="mt-6">
                    <label htmlFor="disaster-select" className="text-lg text-gray-600">Select Disaster Type: </label>
                    <select
                        id="disaster-select"
                        value={disasterType}
                        onChange={handleDisasterTypeChange}
                        className="p-3 ml-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400 text-lg"
                    >
                        <option value="earthquake">Earthquake</option>
                        <option value="storm">Storm</option>
                        <option value="flood">Flood</option>
                        <option value="volcanic">Volcanic Activity</option>
                    </select>
                </div>
            </div>
        </div>
    );
};

export default Graph1;

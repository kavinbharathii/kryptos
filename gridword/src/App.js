import './App.css';
import { useEffect, useState } from 'react';

function App() {
	const [rows, setRows] = useState(1);
	const [columns, setColumns] = useState(1);
	const [prompt, setPrompt] = useState("");
	const [grid, setGrid] = useState([]);

	const makeGrid = () => {
		let newGrid = [];
		for (let i = 0; i < rows; i++) {
			let row = [];
			for (let j = 0; j < columns; j++) {
				row.push('');
			}
			newGrid.push(row);
		}
		setGrid(newGrid);
	}

	function fillGrid() {
		let inputText = prompt;

		let newGrid = [];
		let k = 0;
		for (let i = 0; i < rows; i++) {
			newGrid.push([]);
			for (let j = 0; j < columns; j++) {
				newGrid[i].push(inputText[k]);
				k++;
			}
		}

		setGrid(newGrid)
	}

	useEffect(() => {
		makeGrid()
    fillGrid()
	}, [rows, columns])

	useEffect(() => {
		fillGrid()
	}, [prompt])

	return (
		<div className="App">

			<div>
				{grid.map((row, rowIndex) => {
					return (
						<div key={rowIndex} className='row'>
							{row.map((cell, cellIndex) => {
								return (
									<div key={cellIndex} className="cell">
										{cell}
									</div>
								);
							})}
						</div>
					);
				})}
			</div>


			<div className='gridControls'>
				<input className="rowControl" type="number" value={rows} onChange={(e) => setRows(e.target.value)} />
				<input className="colControl" type="number" value={columns} onChange={(e) => setColumns(e.target.value)} />
				<input className="textControl" placeholder='text here' type="text" value={prompt} onChange={(e) => setPrompt(e.target.value)} />
			</div>

		</div>
	);
}

export default App;

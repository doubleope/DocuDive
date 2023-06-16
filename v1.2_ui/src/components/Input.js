import { useState } from 'react';
import { Dropdown } from 'react-bootstrap';
import storedresponse from '../storedresponse.json';


export default function Input({handleSubmit}) {

    const [userInput, setUserInput] = useState('');

    return (
        <div className='d-flex align-items-center col-11'>
            <div className='mx-5 col-8'>
            <input className='col-12'
                type="text"
                placeholder="Enter a prompt"
                value={userInput}
                onChange={e => setUserInput(e.target.value)}
            />
            </div>

        <Dropdown className='mx-1'>
            <Dropdown.Toggle variant="success" id="dropdown-basic">
                Prepared responses
            </Dropdown.Toggle>

            <Dropdown.Menu>
                {storedresponse.map((response) => (
                    <Dropdown.Item onClick={(e) => { setUserInput(response.prompt); handleSubmit(e, response.prompt, response.result); } }>{response.prompt}</Dropdown.Item>
                ))}
            </Dropdown.Menu>
        </Dropdown>
            
        <button className="btn btn-primary" onClick={(e) => handleSubmit(e, userInput)}>Submit</button>
        </div>
    )
    
}

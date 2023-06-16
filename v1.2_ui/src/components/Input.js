import { useState } from 'react';

export default function Input({handleSubmit}) {

    const [userInput, setUserInput] = useState('')

    return (
        <div className='d-flex align-items-center col-11'>
            <div className='mx-5 col-10'>
            <input className='col-12'
                type="text"
                placeholder="Enter a prompt"
                value={userInput}
                onChange={e => setUserInput(e.target.value)}
            />
            </div>
                <button className="btn btn-primary" onClick={(e) => handleSubmit(e, userInput)}>Submit</button>
        </div>
    )
    
}

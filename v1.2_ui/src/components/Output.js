import './Output.css'

export default function Output({outputText}) {
    return (
        <div className="d-flex justify-content-center w-100 height85 my-5">
            <textarea className="col-10" readonly value={outputText}></textarea>
        </div>
    )
}

import  {useState, useEffect} from 'react'


const Home = () => {
        const [name, setName] = useState('mario');
        
        const handleClick = () => {
                setName('lugigi')
        }

        useEffect(() => {
                 console.log("use Effect run")
        })

        return (
              <div className="home">
                <p>{name}</p>
                <h2>Homepage</h2>
                <button onClick={handleClick}>Click Me</button>
              </div>  
        );
}

export default Home;
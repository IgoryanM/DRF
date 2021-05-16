import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import UserList from './components/Users.js';
import axios from 'axios';
import Navibar from './components/Navibar.js';
import Footer from './components/Footer';


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users')
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error))
    }

    // componentDidMount() {
    //     const users = [
    //         {
    //             "first_name": "test_1",
    //             "last_name": "test_1",
    //             "email": "test1@local.com"
    //         },
    //         {
    //             "first_name": "test_2",
    //             "last_name": "test_2",
    //             "email": "test2@local.com"
    //         },
    //     ]
    //     this.setState(
    //         {
    //             'users': users
    //         }
    //     )
    // }

    render() {
        return (
            <>
            <Navibar/>
            <UserList users={this.state.users}/>
            <Footer/>
            </>
        );
    }
}

export default App;

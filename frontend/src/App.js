import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

import UserList from './components/Users.js';
import ProjectList from './components/Projects';
import NoteList from "./components/Notes";
import LoginForm from './components/Auth.js'


import Navibar from './components/Navibar.js';
import Footer from './components/Footer';
import ProjectTable from "./components/Project";

import axios from 'axios';
import {BrowserRouter, Route, Switch} from 'react-router-dom'
import Cookies from 'universal-cookie';


const NotFound404 = ({location}) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>
    )
}

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'notes': [],
            'token': '',
        }
        this.is_authenticated = this.is_authenticated.bind(this)
        this.logout = this.logout.bind(this)

    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())
    }

    is_authenticated() {
        return this.state.token !== ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
            .then(response => {
                this.set_token(response.data['token'])
            }).catch(error => alert('Неверный логин или пароль'))
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_authenticated()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    load_data() {
        const headers = this.get_headers()

        axios.get('http://127.0.0.1:8000/api/users', {headers})
            .then(response => {
                const users = response.data.results
                this.setState({'users': users})
            }).catch(error => {
            console.log(error)
            this.setState({users: []})
        })

        axios.get('http://127.0.0.1:8000/api/projects', {headers})
            .then(response => {
                const projects = response.data.results
                this.setState({'projects': projects})
            }).catch(error => {
            console.log(error)
            this.setState({projects: []})
        })

        axios.get('http://127.0.0.1:8000/api/notes', {headers})
            .then(response => {
                const notes = response.data.results
                this.setState({'notes': notes})
            }).catch(error => {
            console.log(error)
            this.setState({notes: []})
        })
    }

    componentDidMount() {
        this.get_token_from_storage()
    }

    render() {
        return (
            <div className="App">
                <BrowserRouter>
                    <Navibar is_authenticated={this.is_authenticated} logout={this.logout}/>
                    <Switch>
                        <Route exact path='/' component={() => <UserList users={this.state.users}/>}/>
                        <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects}/>}/>
                        <Route exact path='/notes' component={() => <NoteList notes={this.state.notes}/>}/>
                        <Route path='/projects/project/:id'> <ProjectTable projects={this.state.projects}/> </Route>
                        <Route exact path='/login' component={() => <LoginForm
                            get_token={(username, password) => this.get_token(username, password)}/>}/>
                        <Route component={NotFound404}/>
                    </Switch>
                    <Footer/>
                </BrowserRouter>}
            </div>
        );
    }
}

export default App;

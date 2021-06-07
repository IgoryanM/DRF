import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

import UserList from './components/Users.js';
import ProjectList from './components/Projects';
import NoteList from "./components/Notes";

import Navibar from './components/Navibar.js';
import Footer from './components/Footer';

import axios from 'axios';
import {BrowserRouter, Route, Switch} from 'react-router-dom'
import ProjectTable from "./components/Project";


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
            'notes': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users')
            .then(response => {
                const users = response.data.results
                this.setState({'users': users})
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/projects')
            .then(response => {
                const projects = response.data.results
                this.setState({'projects': projects})
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/notes')
            .then(response => {
                const notes = response.data.results
                this.setState({'notes': notes})
            }).catch(error => console.log(error))
    }

    render() {
        return (
            <div className="App">
                <BrowserRouter>
                    <Navibar/>
                    <Switch>
                        <Route exact path='/' component={() => <UserList users={this.state.users}/>}/>
                        <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects}/>}/>
                        <Route exact path='/notes' component={() => <NoteList notes={this.state.notes}/>}/>
                        <Route path='/projects/project/:id'> <ProjectTable projects={this.state.projects}/> </Route>
                        <Route component={NotFound404}/>
                    </Switch>
                    <Footer/>
                </BrowserRouter>
            </div>
        );
    }
}

export default App;

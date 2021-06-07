import React from 'react'
import {Link} from 'react-router-dom'


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td><Link to={`projects/project/${project.id}`}>{project.title}</Link></td>
            <td>{project.link}</td>
            <td>{project.users}</td>
        </tr>
    )
}


const ProjectList = ({projects}) => {
    return (
        <>
            <h1>Projects list</h1>
            <table>
                <tr>
                    <th>Title</th>
                    <th>Link</th>
                    <th>Users</th>
                </tr>
                {projects.map((project) => <ProjectItem project={project}/>)}
            </table>
        </>
    )
}


export default ProjectList
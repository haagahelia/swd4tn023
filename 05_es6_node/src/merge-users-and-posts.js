const fs = require('fs');

const { getUsers, getPosts } = require('./blog/api');

async function main() {
    let users = await getUsers();
    let posts = await getPosts();

    let { combineUsersAndPosts } = require('./blog/functions');

    let usersAndPosts = combineUsersAndPosts(users, posts);
    let jsonString = JSON.stringify(usersAndPosts, null, 4);

    fs.writeFileSync('output.json', jsonString);
}

main();
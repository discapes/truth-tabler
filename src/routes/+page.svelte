<script lang="ts">
	import program from '$lib/truth_table.py?raw';
	import { loadPyodide, type PyProxyCallable } from 'pyodide';
	import { tick } from 'svelte';
	import { onMount } from 'svelte';

	let mounted = false;
	let input = '(A and A) == ((not C) or A) and im(C, A)';
	let container: HTMLParagraphElement;
	let generate: PyProxyCallable;

	const pPyodide = loadPyodide({
		indexURL: '/pyodide'
	}).then((pyodide) => {
		pyodide.runPython(program);
		generate = pyodide.globals.get('generate');
	});

	$: run(input);

	async function run(statement: string) {
		await pPyodide;
		if (!mounted) return;
		container.innerText = '$' + generate(statement) + '$';
		await tick();
		MathJax.typeset();
	}

	onMount(() => ((mounted = true), run(input)));
</script>

<svelte:head>
	<title>truth-tablez</title>
	<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
	<script>
		MathJax = { tex: { inlineMath: [['$', '$']] } };
	</script>
	<script
		id="MathJax-script"
		async
		src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"
	></script>
</svelte:head>

<div class="w-full flex flex-col items-center justify-center grow">
	<div class="rb flex flex-col gap-5">
		{#await pPyodide}
			Loading pyodide...
		{:then}
			Input:
			<input bind:value={input} />

			Output:
			<p bind:this={container} />
		{/await}
	</div>
</div>

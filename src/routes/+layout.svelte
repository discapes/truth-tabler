<script lang="ts">
	import './app.less';
</script>

<div class="min-h-screen min-w-full inline-flex flex-col text-slate-50">
	<main class="grow bg-slate-700 flex flex-col">
		<slot />
	</main>
	<div class="p-3 text-center bg-slate-800">
		©
		{new Date().getFullYear()}
		Miika Tuominen
	</div>
</div>

<script lang="ts">
	import './app.less';
</script>

<div class="min-h-screen min-w-full inline-flex flex-col text-emerald-50">
	<main class="grow bg-emerald-700 flex flex-col">
		<slot />
	</main>
	<div class="p-3 text-center bg-emerald-800">
		©
		{new Date().getFullYear()}
		Miika Tuominen
	</div>
</div>
